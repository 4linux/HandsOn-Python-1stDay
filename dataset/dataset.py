import sys
from typing import TextIO

from pymongo import MongoClient


SEPARADOR_CSV = "\t"


def converter(csv: TextIO) -> list[dict]:
    headers = next(csv, None)

    if headers is None:
        return []

    cabecalho = headers.strip().split(SEPARADOR_CSV)
    dados = []

    for linha in csv:
        colunas = linha.strip().split(SEPARADOR_CSV)
        documento = zip(cabecalho, colunas)
        documento = dict(documento)
        dados.append(documento)

    return dados


def importar(arquivo: str):
    with open(arquivo) as arq:
        dados = converter(arq)

    if dados == []:
        return None

    with MongoClient() as client:
        db = client["hands-on-python"]
        resultado = db.estoque.insert_many(dados)

    return resultado


def main():
    try:
        nome_arquivo = sys.argv[1]

    except IndexError:
        print("Execute o programa passando",
              "o nome do arquivo CSV")
        return

    resultado = importar(nome_arquivo)

    if resultado is not None:
        if resultado.acknowledged:
            print(len(resultado.inserted_ids),
                  "documentos foram inseridos.")

        else:
            print("Nenhum documento foi inserido.")

    else:
        print("Não há dados para importar.")


if __name__ == "__main__":
    main()
