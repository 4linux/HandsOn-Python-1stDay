from typing import Tuple


escala_imc = {
    "map": "muito abaixo do peso",
    "ap": "abaixo do peso",
    "pi": "peso ideal",
    "ac": "acima do peso",
    "o1": "obesidade 1",
    "o2": "obesidade 2",
    "o3": "obesidade 3"
}

def calcular_imc(peso_kg: float,
                 altura_m: float) -> Tuple[float, str]:

    imc = peso_kg / altura_m ** 2

    if imc < 17:
        situacao = "map"
    elif imc < 18.5:  # else if
        situacao = "ap"
    elif imc < 25:
        situacao = "pi"
    elif imc < 30:
        situacao = "ac"
    elif imc < 35:
        situacao = "o1"
    elif imc < 40:
        situacao = "o2"
    else:
        situacao = "o3"

    saida = (imc, situacao)
    return saida


def main():
    try:
        peso = input("Digite o seu peso em quilos: ")
        peso = float(peso)
        altura = float(input("Digite a sua altura em metros: "))

    except ValueError:
        print("O valor fornecido não é válido")
        return

    resultado = calcular_imc(peso, altura)
    # imc = resultado[0]
    # referencia = resultado[1]
    (imc, referencia) = resultado

    print(referencia)
    situacao = escala_imc[referencia]

    print("O seu imc é", imc)
    print("A sua situação é", situacao)


if __name__ == "__main__":
    main()
