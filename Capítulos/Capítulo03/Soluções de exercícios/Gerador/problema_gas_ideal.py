# encoding utf8
# Este arquivo mostra como utilizar o QuestionGenerator para fazer uma
# pergunta similar àquelas utilizadas no curso.

import random
from copy import deepcopy

from QuestionGenerator import QuestionGenerator, stateDict, OutcomeOfStep

template_str = """\
A fórmula do gás ideal é

$$pV = nRT$$

considerando {m:.3f}g de {nome_do_elemento} a {T_F:.3f}°F em um frasco de {volume_mL:.3f}mL.
Considere a constante dos gases igual a {R} J/(K mol).
Considere a massa molar de {nome_do_elemento} como {MM:.2f} g/mol.
Calcule a pressão em bar.
"""
alternative_str = "{0} {1:.3g} bar\n"
first_state_dict = {
    "m": 3.4,
    "MM": 4.0,
    "T_F": 77,
    "volume_mL": 35,
    "R": 8.314472,
    "nome_do_elemento": "Hélio",
}
number_of_alternatives = 4


class Passo1ConversaoDeVolume:
    def execute(self, state: stateDict, outcome_of_step: OutcomeOfStep) -> stateDict:
        state = deepcopy(state)
        if outcome_of_step == OutcomeOfStep.Correct:
            return self.correto(state)
        else:
            return self.erro1(state)

    def correto(self, state: stateDict) -> stateDict:
        state["V"] = state["volume_mL"] * 1e-6
        return state

    def erro1(self, state: stateDict) -> stateDict:
        state["V"] = state["volume_mL"] * 1e-3
        return state


class Passo2ConversaoDeTemperatura:
    def execute(self, state: stateDict, outcome_of_step: OutcomeOfStep) -> stateDict:
        state = deepcopy(state)
        if outcome_of_step == OutcomeOfStep.Correct:
            return self.correto(state)
        choices = [self.erro1, self.erro2, self.erro3]
        return random.choice(choices)(state)

    def correto(self, state: stateDict) -> stateDict:
        state["T"] = (state["T_F"] - 32) / 9 * 5 + 273.15
        return state

    def erro1(self, state: stateDict) -> stateDict:
        """Esquece de converter F para K"""
        state["T"] = state["T_F"]
        return state

    def erro2(self, state: stateDict) -> stateDict:
        """Esquece de converter C para K"""
        state["T"] = (state["T_F"] - 32) / 9 * 5
        return state

    def erro3(self, state: stateDict) -> stateDict:
        """Utiliza a conversão errada de C para K"""
        state["T"] = (state["T_F"] - 32) / 9 * 5 - 273.14
        return state


class Passo3CalculoNumeroMols:
    def execute(self, state: stateDict, outcome_of_step: OutcomeOfStep) -> stateDict:
        state = deepcopy(state)
        if outcome_of_step == OutcomeOfStep.Correct:
            return self.correto(state)
        else:
            return self.errado(state)

    def correto(self, state: stateDict) -> stateDict:
        state["n"] = state["m"] / state["MM"]
        return state

    def errado(self, state: stateDict) -> stateDict:
        """Erra no cálculo do número de mols"""
        state["n"] = state["m"] * state["MM"]
        return state


class Passo4CalculoGasIdeal:
    """Não possui erro"""

    def execute(self, state: stateDict, outcome_of_step: OutcomeOfStep) -> stateDict:
        state = deepcopy(state)
        return self.correto(state)

    def correto(self, state: stateDict) -> stateDict:
        n = state["n"]
        R = state["R"]
        T = state["T"]
        V = state["V"]
        state["p"] = n * R * T / V
        return state


class Passo5ConversaoPressao:
    def execute(self, state: stateDict, outcome_of_step: OutcomeOfStep) -> stateDict:
        state = deepcopy(state)
        if outcome_of_step == OutcomeOfStep.Correct:
            return self.correto(state)
        else:
            return self.errado(state)

    def correto(self, state: stateDict) -> stateDict:
        state["answer"] = state["p"] / 1e5
        return state

    def errado(self, state: stateDict) -> stateDict:
        """Erra no cálculo do número de mols"""
        state["answer"] = state["p"] / 1e6
        return state


Q = QuestionGenerator(
    template_string=template_str,
    alternative_template_string=alternative_str,
    amount_of_alternatives=4,
    chance_error_during_steps=0.1,
    steps=[
        Passo1ConversaoDeVolume(),
        Passo2ConversaoDeTemperatura(),
        Passo3CalculoNumeroMols(),
        Passo4CalculoGasIdeal(),
        Passo5ConversaoPressao(),
    ],
    state=first_state_dict,
)


if __name__ == "__main__":
    print("-------- Gerando divergências com o mesmo conjunto de dados de entrada --------")
    res1 = Q.generate_question_output(42)
    res2 = Q.generate_question_output(43)
    res3 = Q.generate_question_output(44)
    res4 = Q.generate_question_output(45)

    print(
        "1) " + res1.questionText,
        "2) " + res2.questionText,
        "3) " + res3.questionText,
        "4) " + res4.questionText,
        sep="\n",
    )

    print("GABARITO".center(15, "-"))
    print(1, res1.correctAlternative)
    print(2, res2.correctAlternative)
    print(3, res3.correctAlternative)
    print(4, res4.correctAlternative)

    print("------ Gerando diferentes valores das variáveis ------")
    gases = {"H2": 2, "He": 4.002, "Ne": 20.1797, "Ar": 39.792, "N2": 28.01348}
    massa_min = 1e-3
    massa_max = 10.0
    T_min = 0.0
    T_max = 200.0
    volume_min = 1.0
    volume_max = 100.0

    num_quests = 5
    questoes = []
    for i in range(num_quests):
        state = deepcopy(first_state_dict)
        state["nome_do_elemento"] = random.choice(list(gases.keys()))
        state["MM"] = gases[state["nome_do_elemento"]]
        state["m"] = random.uniform(massa_min, massa_max)
        state["T_F"] = random.uniform(T_min, T_max)
        state["volume_mL"] = random.uniform(volume_min, volume_max)
        Q = QuestionGenerator(
            template_string=template_str,
            alternative_template_string=alternative_str,
            amount_of_alternatives=4,
            chance_error_during_steps=0.1,
            steps=[
                Passo1ConversaoDeVolume(),
                Passo2ConversaoDeTemperatura(),
                Passo3CalculoNumeroMols(),
                Passo4CalculoGasIdeal(),
                Passo5ConversaoPressao(),
            ],
            state=state,
        )
        questoes.append(Q.generate_question_output())

    for i, q in enumerate(questoes):
        print(f"{i+1})", q.questionText)

    print("GABARITO".center(15, "-"))

    for i, q in enumerate(questoes):
        print(i + 1, q.correctAlternative)
