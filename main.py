"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    R = int(input("Qual o raio do circulo?\n"))
    P = math.pi
    A = P * R**2
    print (f"A área do círculo é {A:.2f}.")


if __name__ == '__main__':
    main()
