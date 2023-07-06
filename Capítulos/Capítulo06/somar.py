import sys


def somar(a, b):
    return a + b


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python somar.py (valor1) (valor2)")
        sys.exit(1)
    print(somar(float(sys.argv[1]), float(sys.argv[2])))
