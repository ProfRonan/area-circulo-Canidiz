"""Arquivo principal que será interpretado pelo interpretador."""
import math


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    R = int(input("Qual o raio do circulo?\n"))
    P = math.pi
    A = round(P * R**2,2)
    print (f"A área do circulo é {A}.")


if __name__ == '__main__':
    main()
