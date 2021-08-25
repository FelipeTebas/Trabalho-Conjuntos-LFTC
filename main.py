from conjunto import Conjunto

if __name__ == "__main__":
    try:
        conjuntoA = Conjunto([1, 2, 3, 4, 5, 6])
        conjuntoB = Conjunto([1, 2, 3, 4, 5, 6, 7, 8])
        conjuntoC = Conjunto()
        print('saida:', conjuntoA.tamanho())
        print('saida:', conjuntoA.possui(5))
        print('saida:', conjuntoA.contem_propriamente(conjuntoB))
        print('saida:', conjuntoC.eh_vazio())
        print('saida:', conjuntoA.complemento(conjuntoB))
    except:
        print('Conjunto inválido')
