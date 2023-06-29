from matplotlib import pyplot as plt


def plot_iracema():
    word_list, total_words, total_interesting_words = analyze_iracema_word_count(
        "./dados/iracema.txt"
    )

    fig, ax = plt.subplots()
    xx, yy = list(zip(*word_list[:10]))
    ax.bar(xx, yy)
    ax.set_xticks(ax.get_xticks(), labels=ax.get_xticklabels(), rotation=90)

    fig, ax = plt.subplots()
    ax.barh(xx[::-1], yy[::-1])


def simple_peak_finder(yy, peak=True):
    indexes = []
    for i in range(len(yy)):
        if i == 0 or i == len(yy) - 1:
            continue
        if (yy[i] > yy[i - 1]) and (yy[i] > yy[i + 1]) and peak:
            indexes.append(i)
            continue
        if (yy[i] < yy[i - 1]) and (yy[i] < yy[i + 1]) and (not peak):
            indexes.append(i)
    return indexes


def plot_gaussians():
    xx = [i / 10 for i in range(-50, 80, 1)]
    sigmas = [0.9, 0.9, 0.9, 0.9, 0.9]
    mus = [-2, -1, 0, 1, 2]
    gaussiana_fixa = yy = [
        1 / (1 * (2 * 3.1415) ** 2) * 2.71828 ** (-0.5 * (x - 4.5) ** 2 / 1**2) for x in xx
    ]

    for sigma, mu in zip(sigmas, mus):
        gaussiana_móvel = [
            1 / (sigma * (2 * 3.1415) ** 2) * 2.71828 ** (-0.5 * (x - mu) ** 2 / sigma**2)
            for x in xx
        ]
        yy = [i + j for i, j in zip(gaussiana_fixa, gaussiana_móvel)]

        indices_picos = simple_peak_finder(yy)
        valores_picos = [yy[i] for i in indices_picos]

        indices_vales = simple_peak_finder(yy, peak=False)
        valores_vales = [yy[i] for i in indices_vales]

        print("Picos:", indices_picos, valores_picos)
        print("Vales:", indices_vales, valores_vales)

        fig, ax = plt.subplots()
        ax.bar(xx, yy)


plot_iracema()
plot_gaussians()
