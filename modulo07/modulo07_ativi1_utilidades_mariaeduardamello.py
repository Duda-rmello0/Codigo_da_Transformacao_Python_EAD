'''
Potenciação

Divisão

Multiplicação

Soma

Subtração
'''

def soma(a, b):

    return a + b


def subtrair(a, b):

    return a - b


def multiplicacao(a, b):

    return a * b


def divisao(a, b):

    if b == 0:
        return "Erro: Divisão por Zero não Permitida"
    return a / b


def divisao_inteira(a, b):

    if b == 0:
        return "Erro: Divisão por Zero não Permitida."
    return a // b


def resto_divisao(a, b):

    if b == 0:
        return "Erro: Divisão por zero não permitida."
    return a % b

def potenciacao(base, expoente):

    return base ** expoente

def calcular_media(lista_numeros):

    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)

def e_par(numero):
    return numero % 2 == 0