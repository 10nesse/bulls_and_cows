import random
from colorama import Fore, Style

def generate_number():
    """Генерирует четырехзначное число без повторяющихся цифр"""
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]

def count_bulls_and_cows(secret, guess):
    """Вычисляет количество быков и коров для заданного числа"""
    bulls, cows = 0, 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    """Основная функция игры"""
    secret = generate_number()
    attempts = 0
    print(Fore.GREEN + "Я загадал четырехзначное число. Попробуйте отгадать его." + Style.RESET_ALL)
    while True:
        guess = input("Введите число: ")
        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
            print(Fore.RED + "Введите четырехзначное число без повторяющихся цифр." + Style.RESET_ALL)
            continue
        guess = [int(d) for d in guess]
        bulls, cows = count_bulls_and_cows(secret, guess)
        attempts += 1
        if bulls == 4:
            print(Fore.GREEN + f"Поздравляю! Вы угадали число за {attempts} попыток." + Style.RESET_ALL)
            break
        else:
            print(Fore.YELLOW + f"Быки: {bulls}, коровы: {cows}" + Style.RESET_ALL)

if __name__ == '__main__':
    play_game()
