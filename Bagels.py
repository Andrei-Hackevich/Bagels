import random

max_digit = 3  # количество цифр в загаданном числе
max_guesses = 10  # количество попыток

# Процесс игры
def game():
    while True:
        num = get_num()
        secret_num(num)
        agree = input('Хотите сыграть еще? y/n: ')
        if agree == 'n':
            print('Приходите к нам еще!!!')
            break


# Функция, которая генерирует загаданное число
def get_num():
    num = random.randint(0, 1000)
    number = str(num)
    if len(number) == 1:
        number = '00' + number
    elif len(number) == 2:
        number = '0' + number
    return number

# Процесс отгадки загаданного числа:
def secret_num(num):
    for i in range(0, max_guesses):
        print(f'Попытка {i + 1}')
        while True:
            choice = input('Введите ваше число: ')
            if len(choice) == max_digit and choice.isdecimal():
                break
        if choice == num:
            print('Вы угадали правильное число!!! Поздравляем!!!')
            break
        elif choice[0] in num or choice[1] in num or choice[2] in num:
            for j in range(0, max_digit):
                if choice[j] in num and choice[j] != num[j]:
                    print('Pico', end=' ')
                elif choice[j] == num[j]:
                    print('Fermi', end=' ')
            print('')

        else:
            print('Bagels')

    if choice != num:
        print(f'К сожалению Вы не угадали загаданное число: {num}')

game()
