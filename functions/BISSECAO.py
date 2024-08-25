from math import sin, cos, tan, exp
import sys

#FUNCAO DE DEFINICAO DO PROBLEMA
def bissecao(equacao):
    print('#' * 100)
    print('METODO DE BISSECAO')
    print('#' * 100)

    # INSERCAO DE DADOS DE ENTRADA
    print('Entrada:')
    print('#' * 100)

    x0 = float(input('Valor inicial x0: '))
    x1 = float(input('Valor inicial x1: '))
    tolerancia = float(input('Tolerancia: '))
    limite = int(input('Limite de iteracoes: '))
    i = 0
    sys.setrecursionlimit(limite*2)
    print('#' * 100)
    print('ITERACOES')
    print('#' * 100)
    iteracao(equacao, tolerancia, i, limite, x0, x1)

def iteracao(equacao, tolerancia, i, lim, x0, x1):
    #EXIBICAO DE DADOS INICIAIS
    print('#' * 100)

    fx = []  # VARIAVEL PARA ARMAZENAMENTO DE RESULTADOS DA FUNCAO

    # CONDICAO DE PARADA
    if i >= lim:
        return [x0, x1, i]

    # CALCULOS DA EQUACAO
    x = x0
    fx.append(eval(equacao))
    x = x1
    fx.append(eval(equacao))

    #EXIBICAO DE RESULTADOS INSTANTANEOS
    print(f'Iteracao: {i}')
    print(f'x0: {x0} | f(x0): {fx[0]}')
    print(f'x1: {x1} | f(x1): {fx[1]}')

    #VERIFICACAO DE RAIZ
    if (abs(fx[0]) <= tolerancia):
        print(f'{abs(fx[0])} < {tolerancia}')
        print(f'Finalizado para raiz = {x0}')
        print('#' * 100)
        return [x0, i]

    elif (abs(fx[1]) <= tolerancia):
        print(f'{abs(fx[1])} < {tolerancia}')
        print(f'Finalizado para raiz = {x1}')
        print('#' * 100)
        return [x1, i]
    else:
        x2 = (x0 + x1) / 2
        x = x2
        fx.append(eval(equacao))

        if fx[0] * fx[2] < 0:
            return iteracao(equacao, tolerancia, i+1, lim, x0, x2)
        else:
            return iteracao(equacao, tolerancia, i+1, lim, x2, x1)
