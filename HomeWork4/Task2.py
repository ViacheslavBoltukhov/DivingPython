'''
Вы пришли на работу в компанию по разработке игр, целевая аудитория —
дети и их родители. У предыдущего программиста было задание сделать две
игры в одном приложении, чтобы пользователь мог выбирать одну из них.
Однако программист, на место которого вы пришли, перед увольнением не
успел выполнить эту задачу и оставил только небольшой шаблон проекта.
Используя этот шаблон, реализуйте игры «Камень, ножницы, бумага» и «Угадай
число».
Правила игры «Камень, ножницы, бумага»: программа запрашивает у
пользователя строку и выводит, победил он или проиграл. Камень бьёт
ножницы, ножницы режут бумагу, бумага кроет камень.
Правила игры «Угадай число»: программа запрашивает у пользователя число
до тех пор, пока он не отгадает загаданное
'''
from random import randint


def rock_paper_scissors():
    player = int(input('Choose:\n'
                       '1 - rock\n'
                       '2 - scissors\n'
                       '3 - paper\n'))
    computer = randint(1, 3)
    if player < 1 or player > 3:
        print('Command error, please enter new game')
    elif player == computer:
        print('Draw')
    elif player == 1 and computer == 2 or \
            player == 2 and computer == 3 or \
            player == 3 and computer == 1:
        print('You win')
    else:
        print('You lose')


def guess_the_number():
    number = randint(1, 100)
    while True:
        guess_num = int(input('Enter the number: '))
        if guess_num > number:
            print('Your number is bigger than the one I had in mind')
        elif guess_num < number:
            print('Your number is less than the one I had in mind')
        else:
            print('You win')
            break


def main_menu():
    while True:
        menu = int(input('Choose a game:\n'
                         '1 - rock, paper, scissors\n'
                         '2 - guess the number\n'))
        if menu == 1:
            rock_paper_scissors()
        elif menu == 2:
            guess_the_number()
        else:
            print('The game was not found')
        new_game = int(input('Do you want to play again:\n'
                             '1 - Yes\n'
                             'any other symbol - No\n'))
        if new_game != 1:
            break


if __name__ == '__main__':
    main_menu()
