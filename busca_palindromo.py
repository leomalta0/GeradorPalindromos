import sys

def le_arquivo(palavras_arquivo):
    try:
        with open(palavras_arquivo, 'r') as f:
            palavras = tuple(f.read().splitlines())
            return palavras
    except IOError as e:
        print("{}\nErro ao abrir o arquivo {}. Encerrando programa.".format(e, palavras_arquivo),
              palavras_arquivo=sys.stderr)
        sys.exit(1)

def main():
    palavras = le_arquivo('2. Palíndromos/lista_palavras_ingles.txt')
    lista_palindromos = []

    for palavra in palavras:
        if len(palavra) > 1 and palavra == palavra[::-1]:
            lista_palindromos.append(palavra)

    print("{} palíndromos encontrados.".format(len(lista_palindromos)))
    print(*lista_palindromos, sep='\n')

if __name__ == "__main__":
    main()
