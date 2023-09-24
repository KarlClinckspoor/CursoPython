class ErroComprimentoPalindromo(Exception):
    pass


class ErroNumeroPalindromo(Exception):
    pass


def checar_palindromo(string):
    if (len(string) == 0) or (len(string) > 100):
        raise ErroComprimentoPalindromo("O comprimento da string precisa ser maior que 0!")
    if any(i.isnumeric() for i in string):
        raise ErroNumeroPalindromo("A string não pode conter qualquer número!")

    sanitizada = string.strip().lower()
    for pontuação in ",.!?-;: ":
        sanitizada = sanitizada.replace(pontuação, "")
    reversa = sanitizada[::-1]
    return sanitizada == sanitizada[::-1]


checar_palindromo("101")
