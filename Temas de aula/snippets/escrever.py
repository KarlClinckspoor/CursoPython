# Como escrever resultados
resultados = [1, 2, 3]
erros = [0.1, 0.2, 0.3]

fhand = open('teste.txt', 'w')

for r, e in zip(resultados, erros):
    fhand.write(f'{r}+/-{e}\n')
    
fhand.close()