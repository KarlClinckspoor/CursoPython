
class dadoSAXS:
    """Conjunto de dados e métodos para avaliação de curvas de SAXS."""
    # A função __init__ é acionada quando um objeto é criado.
    def __init__(self, file, load=True, I=[], q=[]):
        if load:
            self.q, self.I = self.load_data(file)
        else:
            self.q, self.I = q, I
    
    # Funções de forma geral podem ser envolvidas por um ou mais decoradores,
    # que afetam o comportamento da função
    @staticmethod
    def load_data(data):
        with open(data) as fhand:
            x, y = [], []
            for line in fhand:
                tx, ty = line.lstrip().replace('  ', ' ').split(' ')
                tx, ty = float(tx), float(ty)
                x.append(tx)
                y.append(ty)
        return x, y
    
    # A palavra chave self é sempre necessária (a não ser que seja um staticmethod)
    # E ela permite que você acesse as propriedades da instância específica do objeto
    # O primeiro argumento é sempre o self, que tem esse nome por convenção,
    # mas você pode mudá-lo.
    # O termo **kwargs é utilizado para passar outros argumentos opcionais para a função
    # plot, para poder especificar linestyle, color, etc.
    def plot(self, xscale='linear', yscale='linear', figsize=(6,4), **kwargs):
        import matplotlib.pyplot as plt
        plt.figure(figsize=figsize)
        plt.plot(self.q, self.I, **kwargs)
        plt.xscale(xscale)
        plt.yscale(yscale)
        plt.show()
    
    # Você pode fazer algo chamado de "method overloading", onde você atribui uma
    # função a algum método interno do Python. Aqui, substituirei o método "-",
    # para subtrair duas curvas de SAXS e colocar em uma terceira.
    def __sub__(self, other):
        sub = [i - j for i, j in zip(self.I, other.I)]
        new = dadoSAXS('', load=False, I=sub, q=self.q)
        return new

# Vamos salvar essa classe para poder importá-la posteriormente, utilizando
# um magic command. Isso irá pegar o primeiro "In" e salvar num script.