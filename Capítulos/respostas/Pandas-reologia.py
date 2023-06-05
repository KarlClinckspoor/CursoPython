df = pd.read_csv('./dados-2/Reologia.txt', 
                 names=['num_exp', 'GP', 'Eta', 'w', 'G1', 'G2', 'T', 'Tau', 'lixo2'],
                 encoding='latin1',
                header=4,
                sep=';',
                decimal=',',
                na_values=' ')

OT_f = df['num_exp'].str.startswith('1')
OF_f = df['num_exp'].str.startswith('2')
CF_f = df['num_exp'].str.startswith('3')

OT = df[OT_f][['Tau', 'G1', 'G2']]
OF = df[OF_f][['w', 'G1', 'G2']]
CF = df[CF_f][['GP', 'Eta']]