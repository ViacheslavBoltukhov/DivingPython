'''
Напишите скрипт, который принимает два аргумента командной строки: число и
строку. Добавьте следующие опции:
● --verbose, если этот флаг установлен, скрипт должен выводить
дополнительную информацию о процессе.
● --repeat, если этот параметр установлен, он должен указывать,
сколько раз повторить строку в выводе.
'''

import argparse


def main():
    """Accepts two command-line arguments: a number and a string.
    Displays additional information about the process if the --verbose flag is set.
    Specifies how many times to repeat a line in the output if the --repeat parameter is set.
    """
    parse = argparse.ArgumentParser(description='Processing numbers and strings with additional options.')
    parse.add_argument('number', type=int, help='The number to output')
    parse.add_argument('text', type=str, help='The output string')
    parse.add_argument('--verbose', action='store_true', help='Output of additional information')
    parse.add_argument('--repeat', type=int, default=1, help='The number of repetitions of the line')
    args = parse.parse_args()
    if args.verbose:
        print(f'Arguments: number={args.number}, text="{args.text}", repeat={args.repeat}')
    print(f'Number: {args.number}, String: {args.text * args.repeat}')


if __name__ == '__main__':
    main()
