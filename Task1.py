'''import re


def checkstr(text: str):
    regex = re.compile('[^a-zA-Z ]')  # Задаем что остается в отфильтрованной строке
    return regex.sub('', text).lower()  # из строки убираем, все кроме того, что указали в в 4 строоке


if __name__ == '__main__':
    print(checkstr(''))'''

'''from string import ascii_letters


def checkstr(text: str):
    return ''.join(let for let in text.lower() if let in ascii_letters + ' ')


if __name__ == '__main__':
    print(checkstr(''))'''

