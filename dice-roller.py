from random import randint


def d20():
    return randint(1, 20)


def d6():
    return randint(1, 6)


def d10():
    return randint(1, 10)


def d4():
    return randint(1, 4)


def d8():
    return randint(1, 8)


def d100():
    return randint(1, 100)

def welcome():
    print "Welcome to dice roller"
    msg = "1: d4\t2: d6\t3: d8\t4: d20\t5: d100\nSelect an option (0 to quit):\n:: "
    user_input = 1
    while user_input != 0:
        try:
            user_input = int(raw_input(msg))
            if user_input == 1:
                print "\n--", d4(), "--\n"
            elif user_input == 2:
                print "\n--", d6(), "--\n"
            elif user_input == 3:
                print "\n--", d8(), "--\n"
            elif user_input == 4:
                print "\n--", d20(), "--\n"
            elif user_input == 5:
                print "\n--", d100(), "--\n"
            elif user_input == 0:
                print "Thank you for using dice roller"
            else:
                print "\n-- Unrecognised input. Try again. --\n"
        except:
            print "\n-- Unrecognised input. Try again. --\n"


if __name__ == "__main__":
    welcome()	
