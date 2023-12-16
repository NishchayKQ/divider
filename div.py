from itertools import cycle

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


peeps = int(input_colored("How many people are there? : "))

total = 0
listOfPeeps = []
totalDict = {}

for ara in range(peeps):
    person = input_colored(f"Enter the name of person {ara+1}: ")
    person = next(color_iterator)+person+default_color
    listOfPeeps.append(person)
    print_output("Now enter the expenses paid by " + person)
    if (ara == 0):
        print_note("Note: Just enter all amounts paid by each person.\n"
                   "The program will keep adding them up until you pass a 'blank enter'")
    muns = 0
    while True:
        try:
            temp = input_colored(": ")
            if not temp:
                break
            temp = int(temp)
            total = temp + total
            muns = muns + temp

        except ValueError:
            print_output("invalid input for an integer")

    totalDict.update({person: muns})

perPersonMuns = total / peeps
print_output(f"total is {total} and per head {perPersonMuns}")
toPay = []

for ara in listOfPeeps:
    temp = perPersonMuns - totalDict[ara]
    print_output(f"money to be paid by {ara} is {temp}")
    toPay.append([temp, ara])


toPay.sort()
i = 0  # iterator that needs to be set
j = 0  # iterator indicating loop position
for ara in toPay:
    if ara[0] < 0:
        temp = abs(ara[0])
        try:
            i = j + 1
            while temp > 0:
                if (toPay[i][0] > 0) and (abs(toPay[i][0]) <= temp):
                    temp = temp - toPay[i][0]
                    print_output(
                        f"{ara[1]} receives INR {toPay[i][0]} by {toPay[i][1]}")
                    toPay[i] = [0, 0]
                i = i + 1
        except IndexError:
            i = j + 1
            while temp > 0:
                if (toPay[i][0] > 0) and (abs(toPay[i][0]) <= temp):
                    temp = temp - toPay[i][0]
                    print_output(
                        f"{ara[1]} receives INR {toPay[i][0]} by {toPay[i][1]}")
                    toPay[i] = [0, 0]

                elif toPay[i][0] > 0:
                    print_output(
                        f"{ara[1]} receives INR {temp} by {toPay[i][1]}")
                    toPay[i][0] = toPay[i][0] - temp
                    temp = 0

                i = i + 1

    j = j + 1
