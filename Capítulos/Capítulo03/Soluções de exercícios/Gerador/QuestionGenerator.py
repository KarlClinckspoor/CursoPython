import enum
import random
from copy import deepcopy
from typing import Protocol
import string
from dataclasses import dataclass

stateDict = dict[str, float]


@dataclass
class QuestionOutput:
    """Meant to hold the output of a QuestionGenerator generate_question_string"""

    correctAlternative: str
    questionText: str
    all_states: dict[str, stateDict]


class OutcomeOfStep(enum.StrEnum):
    """Holds the possible outcomes of a step. Currently, steps can only
    be forced to be correct or make a mistake."""

    Correct = "Correct"
    Wrong = "Wrong"


class SolutionStepProtocol(Protocol):
    """Specifies the function signature of a solution step."""

    def execute(self, state: stateDict, outcome_of_step: OutcomeOfStep) -> stateDict:
        ...


class CantCreateAllErroneousStatesException(Exception):
    pass


class QuestionGenerator:
    def __init__(
        self,
        template_string: str,
        alternative_template_string: str,
        state: stateDict,
        steps: list[SolutionStepProtocol],
        amount_of_alternatives: int = 4,
        chance_error_during_steps: float = 0.1,
    ):
        """
        Creates a question generator

        :param template_string: A string containing the appropriate markings
        so that `.format(state)` will be applied. The answers will be added later.
        :param alternative_template_string: String template that specifies the formatting of the
        alternatives, like number of decimal places, and separators.
        :param state: A dict that contains keys to variable names, like constants,
        initial parameters. These will be passed to the steps, so they can solve the problem
        :param steps: a list of steps that will be executed in sequence, in order to generate
        the answers. One will always be correct, the others will be wrong.
        :param amount_of_alternatives: Number of alternatives in the question, marked a), b), ...
        :param chance_error_during_steps: Chance of commiting an error during the steps.

        To generate the question itself, call generate_question_output
        """
        self._question_template_string = template_string
        self._alternative_template_string = alternative_template_string
        self._initial_state = deepcopy(state)
        self._steps = steps
        self._amount_of_alternatives = amount_of_alternatives
        self._chance_error_during_steps = chance_error_during_steps
        self.key_for_answer = "answer"
        self._safety_iter = 100

    sequence_for_alternatives = [f"{i})" for i in string.ascii_lowercase]

    def _calculate_correct_state(self) -> stateDict:
        """Calculates the correct state by forcing the outcomes of all steps to be correct"""
        correct_state = deepcopy(self._initial_state)
        for step in self._steps:
            correct_state = step.execute(correct_state, outcome_of_step=OutcomeOfStep.Correct)
        return correct_state

    def _calculate_wrong_states(self, correct_state: stateDict) -> list[stateDict]:
        """Calculates only wrong states by discarding states that are either accidentally
        correct or were calculated before (no repeated states).

        Throws CantCreateAllErroneousStatesException in case it couldn't create enough
        erroneous states after _safety_iter iterations.
        """
        wrong_states: list[stateDict] = []
        wrong_answers: list = []
        correct_answer = correct_state[self.key_for_answer]

        for i in range(self._safety_iter):
            # Create only the requested number of alternatives
            if len(wrong_states) >= self._amount_of_alternatives - 1:
                break

            state = deepcopy(self._initial_state)
            for j, step in enumerate(self._steps):
                type_of_step = (
                    OutcomeOfStep.Wrong
                    if random.random() < self._chance_error_during_steps
                    else OutcomeOfStep.Correct
                )
                state = step.execute(state, type_of_step)

            answer = state[self.key_for_answer]
            if answer == correct_answer:  # Didn't make a mistake? Must.
                continue
            elif answer in wrong_answers:  # Made the same mistake? Try again.
                continue
            else:
                wrong_states.append(state)
                wrong_answers.append(answer)
        else:
            raise CantCreateAllErroneousStatesException()

        return wrong_states

    def _format_question_main_body(self) -> str:
        return self._question_template_string.format(**self._initial_state)

    def _format_alternatives(self, all_states_with_letters: dict[str, stateDict]) -> str:
        return "".join(
            [
                self._alternative_template_string.format(letter, state[self.key_for_answer])
                for letter, state in all_states_with_letters.items()
            ]
        )

    def generate_question_output(self, seed: int | None = None) -> QuestionOutput:
        """
        Generates a question body and a sequence of alternatives, where one of them
        is correct and the other are wrong. Returns a QuestionOutput object that
        contains the correct letter, the question string, and all the states
        used to generate the question, in a dict by their letter.

        :param seed: Can be used to set the seed of the random number generator
        :return: QuestionOutput instance.
        """
        if seed:
            random.seed(seed)

        correct_state = self._calculate_correct_state()
        wrong_states = self._calculate_wrong_states(correct_state)
        all_states = [correct_state, *wrong_states]

        random.shuffle(all_states)
        all_states_with_letters = {
            letter: state
            for letter, state in zip(QuestionGenerator.sequence_for_alternatives, all_states)
        }
        correct_letter = [
            letter
            for letter, state in all_states_with_letters.items()
            if state[self.key_for_answer] == correct_state[self.key_for_answer]
        ][0]

        question_string = self._format_question_main_body()
        alternatives_string = self._format_alternatives(all_states_with_letters)
        final_string = question_string + alternatives_string

        return QuestionOutput(correct_letter, final_string, all_states_with_letters)
