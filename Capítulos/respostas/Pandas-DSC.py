df = pd.read_csv('./dados-2/DSC.txt', header=50, names=['t', 'T', 'Q', 'f'], sep=' ')
DSC = df[['T', 'Q']]