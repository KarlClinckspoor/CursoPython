def der_simples(x, y):
    deriv = []
    for i, val in enumerate(x):
        if i == len(x) - 1:
            continue
        d = (y[i + 1] - y[i])/(x[i + 1] - x[i])
        deriv.append(d)
    return deriv


def der_media(x, y):
    deriv = []
    for i, val in enumerate(x):
        if i == 0:
            d = (y[1] - y[0]) / (x[1] - x[0])
        elif i == len(x) - 1:
            d = (y[-1] - y[-2]) / (x[-1] - x[-2])
        else:
            d = 1/2 * ( (y[i+1] - y[i]) / (x[i+1] - x[i]) + ( y[i] - y[i-1]) / (x[i] - x[i-1]) )
        deriv.append(d)
    return deriv