import random
import uuid


def create_csv(
    seed: int | None = None,
    filename: str | None = None,
    length: int = 20,
    sep: str = ",",
    columns: list[str] | None = None,
    converter: bool = False,
):
    if filename is None:
        filename = str(uuid.uuid1()) + ".csv"
    if seed is not None:
        random.seed(seed)
    if columns is None:
        columns = ["col1", "col2", "col3", "col4", "col5"]
    ncol = len(columns)

    with open(f"{filename}", "w", encoding="utf8") as fhand:
        fhand.write(sep.join(columns))
        fhand.write("\n")

        for linenum in range(length):
            line = sep.join(
                [_convert_float_to_str(random.random(), converter) for _ in range(ncol)]
            )
            fhand.write(line)
            fhand.write("\n")


def _convert_float_to_str(f: float, flag: bool):
    if flag:
        return str(f).replace(".", ",")
    return str(f)


def gerar_arquivos_exercício():
    create_csv(seed=42, filename="exercício1.csv", length=20, sep=",")
    create_csv(seed=42, filename="exercício2.csv", length=20, sep=";", converter=True)


if __name__ == "__main__":
    while True:
        escolha = input(
            "Deseja gerar "
            "(a) um conjunto padrão de arquivos, ou "
            "(b) um arquivo genérico? Digite nada para sair."
        )
        if not escolha:
            break
        if escolha == "a":
            gerar_arquivos_exercício()
            break
        elif escolha == "b":
            create_csv(length=random.randint(a=5, b=1000))
            break
        else:
            print(f"Escolha ({escolha}) não reconhecida, tente novamente.")
