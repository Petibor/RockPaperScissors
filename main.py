import random;
from time import sleep

from os import system, name


def whowins(chosen, input1):

    if chosen == input1:
        print(" Hey that's a tie")
    elif (chosen == 1 and input1 == 3) or (chosen == 2 and input1 == 1) or (chosen == 3 and input1 == 2):
        return "**************I win. Ha-Ha**************"
    else:
        return "**************You win. I bet you cheated!!**************"
    print("\n")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    while True:
        chosen = random.randint(1, 3)
        # 1 is rock 2 is paper 3 is scissors
        print("I chose mine. Lets hear yours")
        print("\n")
        print("I choose " + str(chosen))
        print("Press 1 for rock, 2 for paper and 3 for scissors and type exit to end program");
        input1 = input();
        if input1 == "1" or input1 == "2" or input1 == "3":
            print(whowins(chosen, int(input1)))
        elif input1 == "exit":
            break
        else:
            print("Please enter a valid value and try again")
            print("\n")
            sleep(2)
            clear()


if __name__ == '__main__':
    main()
