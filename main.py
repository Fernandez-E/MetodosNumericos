from functions.BISSECAO import bissecao
from functions.INTERPOLACAO_LINEAR import interpolacao_linear
from functions.NEWTON import newton
from functions.SECANTES import secantes

print('#'*100)
print('SOLUÇÃO NUMÉRICA DE EQUAÇÕES NÃO-LINEARES')
print('#'*100)
option = 999

# RESUMO DE SINTAXE PYTHON
print('RESUMO DE FUNCOES PYTHON')
print('#' * 100)
print('Equacao devera ser escrita em linguagem python')
print('Principais funcoes em python: ')
print(
    'Pontos flutuantes devem utilizar ponto: .\nSoma: +\nSubtracao: -\nMultiplicacao: *\nDivisao: /\nPotência: **')
print('Seno: sin(x)\nCosseno: cos(x)\nTangente: tan(x)\ne: exp(x)')
print('#' * 100)

print('Informe a equacao com a variavel sendo escrita OBRIGATORIAMENTE como "x"')
equacao = input('>>> ').lower()

while option != 0:
    print('Qual metodo deseja utilizar?')
    print('1 - Bissecao')
    option = int(input('>>> '))
    if option == 1:
        print()
        bissecao(equacao)
