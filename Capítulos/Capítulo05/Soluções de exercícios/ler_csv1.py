def ler_csv1(arquivo):
    handle = open(arquivo, "r", encoding="utf8")
    conteúdo = handle.readlines()
    cabeçalho = conteúdo[0].strip()
    nomes_das_colunas = cabeçalho.split(",")
    linhas = conteúdo[1:]
    resultado = {coluna: [] for coluna in nomes_das_colunas}
    for linha in linhas:
        dados = linha.strip().split(",")
        for coluna, dado in zip(nomes_das_colunas, dados):
            resultado[coluna].append(float(dado))
    return resultado


ler_csv_simples("./dados/exercício1.csv")
