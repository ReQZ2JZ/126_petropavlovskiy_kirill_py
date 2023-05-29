import random

def write_results_to_file(username, attempts):
    with open('game.txt', 'a') as f:
        f.write(f'Имя: {username}, Количество попыток: {attempts}\n')


username = input("Введите ваше имя: ")

secret_number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Угадайте число от 1 до 100: "))
    attempts += 1

    if guess == secret_number:
        print("Вы угадали число!")
        print("Количество попыток:", attempts)
        write_results_to_file(username, attempts)
        break
    elif guess < secret_number:
        print("Задуманное число больше вашего ответа.")
    else:
        print("Задуманное число меньше вашего ответа.")