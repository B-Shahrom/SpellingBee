import math
import random

from contestants.contestants_manager import read_names, add_name, remove_name, select_random_name

contestants = read_names()
words = ["hello", "how", "are", "you"]

def game_loop():
    while True:
        a_word = random.choice(words)
        print(a_word)
        contestant_answer = input(": ")

        if (a_word == contestant_answer):
            print("Lucky guess")
        else:
            break
    print("We are done here")

def _contestants_manager_console():

    print(" = CONTESTANTS MANAGER CONSOLE = \n = add \ remove \ list \ random \ exit = ")

    while True:
        command_line = input("Your command: ")

        command = command_line.split()[0]
        command = command.lower()
        command_line = command_line.split()[1:]

        if command == "add":
            add_name(command_line[0])
        elif command == "remove":
            remove_name(command_line[0])
        elif command == "list":
            print(read_names())
        elif command == "random":
            print(select_random_name())
        elif command == "exit":
            break
        else:
            print("Unrecoginzed command, (exit) to leave")


    pass

if __name__ == '__main__':
    _contestants_manager_console()


