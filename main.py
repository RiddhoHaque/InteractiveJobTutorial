import sys


def take_input():
    print('Enter the first number for the operation: ')
    num1 = float(input())
    print('Enter the second number for the operation: ')
    num2 = float(input())
    return num1, num2


def main(args):
    print('Arguments:', args)
    if len(args) < 1:
        print('Not enough arguments')
        exit(0)
    if len(args) > 1:
        print('Too many arguments')
        exit(0)
    if args[0] == '+':
        print('Selected Operation: Addition')
        operand1, operand2 = take_input()
        print('The result of the operation is', operand1 + operand2)
    elif args[0] == '-':
        print('Selected Operation: Subtraction')
        operand1, operand2 = take_input()
        print('The result of the operation is', operand1 - operand2)
    elif args[0] == 'X':
        print('Selected Operation: Multiplication')
        operand1, operand2 = take_input()
        print('The result of the operation is', operand1 * operand2)
    else:
        print('Unsupported Operation')


if __name__ == '__main__':
    main(sys.argv[1: ])