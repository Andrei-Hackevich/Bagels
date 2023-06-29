import random

max_digit = 3 # количество цифр в загаданном числе
max_guesses = 10 # количество попыток

def game():
    while True:
        num = get_num()

# Функция, которая генерирует загаданное число
def get_num():
    num = random.randint(0, 1000)
    number = str(num)
    if len(number) == 1:
        number = '00' + number
    elif len(number) == 2:
        number = '0' + number
    return number






