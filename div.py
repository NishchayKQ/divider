from itertools import cycle
from fractions import Fraction

default_color = "\033[0m"
input_color = "\033[38;2;52;101;164m"
output_color = "\033[38;2;85;85;85m"
plsNote_color = "\033[38;2;245;121;0m"
color_iterator = cycle(["\033[38;2;170;0;0m",
                       "\033[38;2;0;170;0m",
                        "\033[38;2;170;85;0m",
                        "\033[38;2;0;0;170m",
                        "\033[38;2;170;0;170m",
                        "\033[38;2;0;170;170m",
                        "\033[38;2;255;255;128m"])


def input_colored(text: str) -> str:
    return input(input_color+text+default_color)


def print_output(text: str) -> None:
    print(output_color+text+default_color)


def print_note(text: str) -> None:
    print(plsNote_color+text+default_color)


peeps = int(input_colored("\nHow many people are there? : "))

total = Fraction("0")
listOfPeeps = []
totalDict = {}

print_note("\nNote: Just enter all amounts paid by each person.\n"
           "The program will keep adding them up until you\n"
           "pass a 'blank enter'\n")

for ara in range(peeps):
    person = input_colored(f"Enter the name of person {ara+1}: ")
    person = next(color_iterator)+person+default_color
    listOfPeeps.append(person)
    print_output("Now enter the expenses paid by " + person)
    muns = Fraction("0")
    while True:
        try:
            temp = input_colored(": ")
            if not temp:
                break
            temp = Fraction(temp)
            total = temp + total
            muns = muns + temp

        except ValueError:
            print_note("invalid input for a number")

    totalDict.update({person: muns})

perPersonMuns = Fraction(total / peeps)
print_output(f"total is {format(total, ',.2f')}\n"
             f"per head its {format(perPersonMuns, ',.2f')}")
toPay = []

print_note("\nbelow are the total amount each of you should\n"
           "pay / recieve. You can use this to verify that\n"
           "all dues have been cleared!\n")

for ara in listOfPeeps:
    temp = Fraction(perPersonMuns - totalDict[ara])
    if temp > 0:
        print_output(f"\t{ara} has to pay {format(temp, ',.2f')}")
    elif temp < 0:
        print_output(f"\t{ara} has to receive {format(abs(temp), ',.2f')}")
    else:
        print_output(f"\t{ara} will not have to pay / receive anything!")
    toPay.append([temp, ara])

print()

toPay.sort()
i = 0  # iterator that needs to be set
j = 0  # iterator indicating loop position
print_note("below are the exact transactions your group has to perform\n"
           "so that there are no dues left!\n")
for ara in toPay:
    if ara[0] < 0:
        temp = Fraction(abs(ara[0]))
        try:
            i = j + 1
            while temp > 0:
                if (toPay[i][0] > 0) and (abs(toPay[i][0]) <= temp):
                    temp = temp - toPay[i][0]

                    print_output(f"\t{toPay[i][1]} pays INR "
                                 f"{format(toPay[i][0], ',.2f')} to "
                                 f"{ara[1]}")

                    toPay[i] = [0, 0]
                i = i + 1
        except IndexError:
            i = j + 1
            while temp > 0:
                if (toPay[i][0] > 0) and (abs(toPay[i][0]) <= temp):
                    temp = temp - toPay[i][0]

                    print_output(f"\t{toPay[i][1]} pays INR "
                                 f"{format(toPay[i][0], ',.2f')} to "
                                 f"{ara[1]}")

                    toPay[i] = [0, 0]

                elif toPay[i][0] > 0:

                    print_output(f"\t{toPay[i][1]} pays INR "
                                 f"{format(temp, ',.2f')} to "
                                 f"{ara[1]}")

                    toPay[i][0] = toPay[i][0] - temp
                    temp = Fraction(0)

                i = i + 1

    j = j + 1
print()
