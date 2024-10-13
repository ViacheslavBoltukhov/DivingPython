'''
Напишите код, который запускается из командной строки и получает на вход путь
до директории на ПК. Соберите информацию о содержимом в виде объектов
namedtuple. Каждый объект хранит: имя файла без расширения или название
каталога, расширение, если это файл, флаг каталога, название родительского
каталога. В процессе сбора сохраните данные в текстовый файл используя
логирование.
'''



from collections import namedtuple
from argparse import ArgumentParser
import os
import logging

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])
logging.basicConfig(filename='log_directory.log', level=logging.INFO, format='%(asctime)s - %(message)s')


def info(directory):
    """Collects information about the contents of the directory and saves it to the log."""
    if not os.path.isdir(directory):
        raise ValueError(f"The specified path {directory} it is not a directory.")
    parent_directory = os.path.basename(os.path.abspath(directory))
    for enter in os.listdir(directory):
        enter_path = os.path.join(directory, enter)
        if os.path.isdir(enter_path):
            file_info = FileInfo(name=enter, extension=None, is_directory=True, parent_directory=parent_directory)
        else:
            name, increase = os.path.splitext(enter)
            file_info = FileInfo(name=name, extension=increase.lstrip('.'), is_directory=False,
                                 parent_directory=parent_directory)
        logging.info(f'{file_info.name} | {file_info.extension if
        file_info.extension else "N/A"} | {"Directory" if
        file_info.is_directory else "File"} | {file_info.parent_directory}')


def main():
    """A function for processing the command line and collecting information."""
    parse = ArgumentParser(
        description="Collecting information about the contents of the directory and writing to the log.")
    parse.add_argument('directory', type=str, help="The path to the directory")
    args = parse.parse_args()
    directory = args.directory
    try:
        info(directory)
        print(f'Information about the contents of the directory "{directory}" '
              f'successfully written to a file directory_contents.log".')
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
