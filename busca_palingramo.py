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

def encontra_palingramos():
    lista_palavras = le_arquivo('lista_palavras_portugues.txt')
    palavras = set(lista_palavras) # Usar set para otimizar o tempo de execução.
    lista_palingramos = []

    for palavra in palavras:
        comprimento = len(palavra)
        inv_palavra = palavra[::-1]

        if comprimento > 1:
            for i in range(comprimento):
                if palavra[i:] == inv_palavra[:comprimento-i] and inv_palavra[comprimento-i:] in palavras:
                    lista_palingramos.append((palavra, inv_palavra[comprimento-i:]))
                if palavra[:i] == inv_palavra[comprimento-i:] and inv_palavra[:comprimento-i] in palavras:
                    lista_palingramos.append((inv_palavra[:comprimento-i], palavra))
    
    return lista_palingramos

def salva_palingramo(titulo_arquivo, palingramos):
    with open(titulo_arquivo, 'w') as fp:
        fp.write('\n'.join('%s %s' % x for x in palingramos))
    
def main():
    palingramos = encontra_palingramos()
    lista_ordenada = sorted(palingramos)

    for primeiro, segundo in lista_ordenada:
        print("{} {}". format(primeiro, segundo))
        
    print("{} palíngramos encontrados.".format(len(lista_ordenada)))
    salva_palingramo('palingramos_gerados', lista_ordenada)

if __name__ == "__main__":
    main()