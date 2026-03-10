"""
Calculadora Simples com Tratamento de Erros

Este programa implementa uma calculadora em Python capaz de realizar operações matemáticas básicas: soma, subtração,
multiplicação e divisão.

O programa solicita dois números ao usuário e uma operação matemática, executa o cálculo correspondente e exibe o
resultado.

Funcionalidades:
- Operações matemáticas básicas (+, -, *, /)
- Modularização do código utilizando funções
- Validação de entrada do usuário
- Tratamento de exceções com try-except

Exceções tratadas:
- ValueError: quando o usuário digita valores que não são números
- ZeroDivisionError: quando ocorre tentativa de divisão por zero

Este projeto foi desenvolvido como exercício prático de lógica de programação e boas práticas em Python.
"""
TITULO = "Calculadora Simples"
TAMANHO_LINHA = 78


def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a: float, b: float) -> float:
    """Retorna a divisão de dois números."""
    return a / b


def main():
    """Função principal que executa o fluxo do programa."""
    print(TAMANHO_LINHA * "=")
    print(TITULO.center(TAMANHO_LINHA))
    print(TAMANHO_LINHA * "=")

    operacoes = {
        '+': somar,
        '-': subtrair,
        '*': multiplicar,
        '/': dividir
    }

    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        operacao = input("Escolha a operação (+, -, *, /): ").strip()
        segundo_numero = float(input("Digite o segundo número: "))

        print(TAMANHO_LINHA * "=")

        if operacao not in operacoes:
            print("Opção inválida.")
            return

        else:
            funcao = operacoes[operacao]
            resultado = funcao(primeiro_numero, segundo_numero)
            print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")

    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

    print(TAMANHO_LINHA * "=")


if __name__ == '__main__':
    main()
