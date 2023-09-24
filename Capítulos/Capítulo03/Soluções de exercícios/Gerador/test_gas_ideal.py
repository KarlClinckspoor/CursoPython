from problema_gas_ideal import Q
from QuestionGenerator import QuestionGenerator

expected_answer = 602.03310
rtol = 1e-5


def within_rtol(actual, expected, rtol):
    return abs(actual - expected) / expected < rtol


for i in range(100):
    # Check that correct is correct
    response = Q.generate_question_output()
    assert within_rtol(
        response.all_states[response.correctAlternative][Q.key_for_answer], expected_answer, rtol
    )
    # Check that wrong is wrong
    other_letters = QuestionGenerator.sequence_for_alternatives[: len(response.all_states)]
    other_letters.remove(response.correctAlternative)
    for other_letter in other_letters:
        assert not within_rtol(
            response.all_states[other_letter][Q.key_for_answer], expected_answer, rtol
        )
