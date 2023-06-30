def ler_csv2(arquivo, sep_cols=",", sep_dec="."):
    handle = open(arquivo, "r", encoding="utf8")
    conteúdo = handle.readlines()
    cabeçalho = conteúdo[0].strip()
    nomes_das_colunas = cabeçalho.split(sep_cols)
    linhas = conteúdo[1:]
    resultado = {coluna: [] for coluna in nomes_das_colunas}
    for linha in linhas:
        dados = linha.strip().split(sep_cols)
        for coluna, dado in zip(nomes_das_colunas, dados):
            resultado[coluna].append(float(dado.replace(sep_dec, ".")))
    return resultado


ler_csv2("./dados/exercício1.csv", sep_cols=",", sep_dec=".")
ler_csv2("./dados/exercício2.csv", sep_cols=";", sep_dec=",")
