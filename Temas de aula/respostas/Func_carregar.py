def carregar_dados(arquivo):
    fhand = open(arquivo, 'r')
    x = []
    y = []

    for line in fhand:
        if line.startswith('x'):
            continue
        if len(line) < 4:
            continue
        line = line.replace('  ', ' ').rstrip().lstrip()
        temp_x, temp_y = line.split(' ')
        temp_x = float(temp_x)
        temp_y = float(temp_y)

        x.append(temp_x)
        y.append(temp_y)

    fhand.close()
    return x, y