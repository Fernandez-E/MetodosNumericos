from math import sin, cos, tan, exp
import sys

def newton(equacao):
    print('#' * 100)
    print('METODO DE NEWTON-RAPHSON')
    print('#' * 100)

    # INSERCAO DE DADOS DE ENTRADA
    print('Entrada:')
    print('#' * 100)
    print('Informe a derivada da equacao com a variavel sendo escrita OBRIGATORIAMENTE como "x"')
    derivada = input('>>> ').lower()
    x0 = float(input('Valor inicial x0: '))
    tolerancia = float(input('Tolerancia: '))
    limite = int(input('Limite de iteracoes: '))

    i = 0
    sys.setrecursionlimit(limite * 2)

    print('#' * 100)
    print('ITERACOES')
    print('#' * 100)

    iteracao(equacao, derivada, tolerancia, i, limite, x0)


def iteracao(equacao, derivada, tolerancia, i, lim, x0):
    # EXIBICAO DE DADOS INICIAIS
    print('#' * 100)

    fx = []  # VARIAVEL PARA ARMAZENAMENTO DE RESULTADOS DA FUNCAO
    dx = [] # VARIAVEL PARA ARMAZENAMENTO DE RESULTADOS DA DERIVADA DA FUNCAO

    # CONDICAO DE PARADA
    if i >= lim:
        return [x0, i]

    # CALCULOS DA EQUACAO
    x = x0
    fx.append(eval(equacao))
    dx.append(eval(derivada))

    # EXIBICAO DE RESULTADOS INSTANTANEOS
    print(f'Iteracao: {i}')
    print(f"x0: {x0} | f(x0): {fx[0]} | f'(x0): {dx[0]}")

    # VERIFICACAO DE RAIZ
    if (abs(fx[0]) <= tolerancia):
        print(f'{abs(fx[0])} < {tolerancia}')
        print(f'Finalizado para raiz = {x0}')
        print('#' * 100)
        return [x0, i]

    else:
        x1 = x0 - (fx[0] / dx[0])
        x = x1
        fx.append(eval(equacao))

        return iteracao(equacao, derivada, tolerancia, i + 1, lim, x1)
