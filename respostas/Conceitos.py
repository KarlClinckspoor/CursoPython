nota = 90
if nota > 90:
    conceito = 'A'
elif nota > 80:
    conceito = 'B'
elif nota > 70:
    conceito = 'C'
elif nota > 60:
    conceito = 'D'
elif nota > 50:
    conceito = 'E'
else:
    conceito = 'F'

print(f'O conceito da nota {nota} é {conceito}')

# Note que ao invés de ter que testar os limites superiores e inferiores, eu aproveitei a característica dos condicionais
# de, assim que a condição for atendida, o resto do código é ignorado. 
# Então, testando os limites superiores, na ordem decrescente de notas, é possível eliminar bastante digitação extra.