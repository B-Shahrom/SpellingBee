import math
import random

contestants = []
words = ["hello", "how", "are", "you"]

def add_contestants():

    while(True):
        command = input("command: ")
        if command == "add":
            contestant_name = input("name: ")

            contestants.append(contestant_name)

        else:
            break

    print(f"Registred contestants: ", contestants)

    return 1

def game_loop():

    while True:
        a_word = random.choice(words)
        print(a_word)
        contestant_answer = input(": ")

        if (a_word == contestant_answer):
            print("Lucky guess")
        else:
            break
    print("we are done here")


if __name__ == '__main__':

    add_contestants()

    game_loop()

    exit(1)

    print("Start game (1)\nSettings (2)\n: ", end='')
    user_input = int(input())

    if (user_input == 1):
        add_contestants()

