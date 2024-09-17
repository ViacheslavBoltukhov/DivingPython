'''Задание 1. Функцию группового переименования файлов.
Напишите функцию группового переименования файлов. Она должна:
1. принимать параметр желаемое конечное имя файлов. При
переименовании в конце имени добавляется порядковый номер.
2. принимать параметр количество цифр в порядковом номере.
3. принимать параметр расширение исходного файла. Переименование
должно работать только для этих файлов внутри каталога.
4. принимать параметр расширение конечного файла.
5. принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
задания функций пакет для работы с файлами.'''
import os


def batch_rename_files(directory, final_name, num_digits, old_extension, new_extension, name_range):
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"Каталог '{directory}' не найден.")
    files = [f for f in os.listdir(directory) if f.endswith(old_extension)]
    if not files:
        print("Файлы с указанным расширением не найдены.")
    return
    format_string = f"{{:0{num_digits}d}}"
    for index, file_name in enumerate(files, start=1):
        base_name = os.path.splitext(file_name)[0]
        if name_range:
            start, end = name_range
            extracted_name = base_name[start - 1:end]
        else:
            extracted_name = base_name
    new_file_name = f"{extracted_name}{final_name}{format_string.format(index)}{new_extension}"
    old_file_path = os.path.join(directory, file_name)
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(old_file_path, new_file_path)
    print(f"Переименован '{file_name}' в '{new_file_name}'")


if __name__ == "__main__":
    import sys


    if len(sys.argv) != 6:
        print("Usage: python file_rename.py <directory> <final_name>< num_digits > < old_extension > < new_extension >")
    sys.exit(1)
    directory = sys.argv[1]
    final_name = sys.argv[2]
    num_digits = int(sys.argv[3])
    old_extension = sys.argv[4]
    new_extension = sys.argv[5]
    # Например, диапазон [3, 6]
    name_range = [3, 6]
    batch_rename_files(directory, final_name, num_digits,
                       old_extension, new_extension, name_range)
