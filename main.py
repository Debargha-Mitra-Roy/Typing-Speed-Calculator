from tabnanny import check
from time import *
import random


def mistake(partest, usertest):

    error = 0

    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1

    return error


def speed_time(time_start, time_end, user_input):

    time_delay = time_end - time_start
    time_round_off = round(time_delay, 2)
    speed = len(user_input) / time_round_off

    return round(speed)


if __name__ == "__main__":

    while(True):

        check = input("Ready to the Typing Speed Test (yes / no) : ")

        if check == "yes":

            test = random.choice(list(open('file.txt')))

            print("***** Typing Speed *****")
            print()
            print(test)

            time_start = time()

            test_input = input("Enter the above line : ")

            time_end = time()

            print()
            print("Speed : ", speed_time(time_start, time_end, test_input), "word(s) / second")
            print("Error : ", mistake(test, test_input))

        elif check == "no":
            print("Thanks for visiting our program.")
            break

        else:
            print("ERROR !!! Enter 'yes' or 'no'.")
