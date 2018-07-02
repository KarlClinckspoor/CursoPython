df = pd.read_csv('./dados-2/Calorimetria.csv', sep=';', decimal=',')
ITC = df[['Xt (mM)', '∆H (J/mol)']] # Exige utilizar o ∆ no nome.

# Segundo método, fornecendo os nomes
colunas = ['lixo', 'DQ', 'Vol', 'Xt', 'Mt', 'XMT', 'DH', 'Fit', 'Res', 'lixo2']
df = pd.read_csv('./dados-2/Calorimetria.csv', sep=';', decimal=',', names=colunas, header=1)
ITC = df[['Xt', 'DH']]