from colorama import init
from colorama import Fore, Back, Style


def main() -> None:
    init()
    print(Back.RED + Fore.BLACK)
    math()
    mark()
    print('\033[0m')


def calc(operand, n1, n2) -> float:
    match operand:
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2
        case '^':
            return n1 ** n2


def math() -> None:
    try:
        assert (operand := input('Choose the operand [+, -, *, /, ^]: ')) in ('+', '-', '*', '/', '^')
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
    except AssertionError:
        return print('You type not a operand!')
    except TypeError:
        return print('You type not a number!')
    
    try:
        print(calc(operand, num1, num2))
    except ZeroDivisionError:
        print('infinity')
    except ArithmeticError:
        print('Arithmetic Error')
    except Exception as exc:
        print(exc.__class__.__str__)


def mark() -> None:
    mark = input('Give me mark please (1~5)')
    if len(mark) == 1 and mark in '12345':
        print('thank you')


if __name__ == '__main__':
    main()
