__author__ = "Juan Bettinelli"

## Functions

##############################################################
# 1)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 1) \n ")


# import Packeges
from ast import And
from cgi import test
from itertools import count
import random
import string

#  -- well why? :) 

# 1)

# declare Vaiables
RanNuList = []
ListSize = 20

# -- ok, seen that exception variable naming before...

# create Function
def remove_max_vales(I_List: list) -> list:
    """Removes the Largest value Element

    Args:
        I_List - Input List to find and remove the largest value.
    """
    # Start conditions
    I_List.remove(max(I_List))
    return I_List

# var naming not exactly pythonic
# --> 2.5P

# create a list with random numbers
for i in range(ListSize):
    RanNuList.append(random.randint(-100, 100))

# Calling the function
print("The original List:  ", RanNuList)
print("The filltered List: ", remove_max_vales(RanNuList))


##############################################################
# 2)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 2) \n ")

# declare Vaiables
Boolen_List_Size = 10
Ran_Bo_List = []

# Declrare Function
def FindTrue(B_List: list) -> list:
    """Checks if values in list are 'true'.

    Args:
        B_List - Input List to find 'True' values.
    """
    # Start conditions
    i = 0
    True_Values = []
    for i in range(len(B_List)):
        if B_List[i] == True:
            True_Values.append(i)
    return True_Values


# create a list with random numbers (1 or 0)
for i in range(Boolen_List_Size):
    Ran_Bo_List.append(random.randint(0, 1))

# Run the Functin
print("The Input list: ", Ran_Bo_List)
print(
    "The Values in the list that are 'True' have the Indices: ", FindTrue(Ran_Bo_List)
)

# Nice type hints
# testing for value equality is not suggested in python `if object` is usually preferred
# 1P

##############################################################
# 3)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 3) \n ")

# The Fuction
def print_spacer(text):
    print("I got this text: ", text)


# Calling the Funktion
print_spacer("test test")

# Answer:
print(
    "This funktion prints the inputed Variable. It also adds some additional Text to the print: 'I got this text: ' infront of the Variable that will be printet."
)

# True, however the return value is `None`
ret = print_spacer("test")
print(ret)
# --> 0 P

##############################################################
# 4)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 4) \n ")

def sort_remainder(s_list : list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) -> list:
    """Sort list by the remainder of 4.

    Args:
        s_list - Input List to find remainder of 4.
    """
    s_list.sort(key=lambda x: [x % 4, x])
    return s_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sort_remainder(my_list))

# nice style
# the lambda does seem to be a bit complicated though
# --> 2P

#############################################################
# 5)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 5) \n ")


def spacer_text(te_string: str) -> None:
    """Format a string and Print it

    Args:
        te_string - string to be formatted.
    """
    print(
        f"{'#' * (len(te_string)+4)}\n# {te_string} #\n{'#' * (len(te_string)+4)} "
    )
    return None


test_s =  input("Please enter test String\n")  # "test"
spacer_text(test_s)

# --> 3P

#############################################################
# 6)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 6) \n ")

test_text = "My example text. With my creative writing and my great spelling"


def find_in_text(the_text: string = "My example text.", the_word: string = "My") -> int:
    """Count the occorens of a string in a string

    Args:
        the_text - The sting (text) to be seached, the_word - The string (word) to search in Text.
    """
    l_text = the_text.lower()
    l_word = the_word.lower()
    return l_text.count(l_word)


print(find_in_text(test_text, "my"))

# You re-interpreted the excercise.
# Occurences are not the same as counting the 'word'
# I like the styling again :)
# --> 2P

#############################################################
# 7)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 7) \n ")


def check_pw(pw: str = "0000") -> bool:
    """checks if Password is usable

    Args:
        pw - The Password to be checked
    """
    safe = False
    counter = 0
    for v in range(len(pw) - 2):
        if (
            (not pw[v] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"])
            and (
                not pw[v + 2] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"]
            )
        ) and (pw[v + 1] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"]):
            counter += 1

    if (pw[0] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"]) and (
        not pw[1] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"]
    ):
        counter += 1
    if (
        pw[len(pw) - 1] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"]
    ) and (
        not pw[len(pw) - 2] in [",", ".", "!", "@", "#", "$", "_", "-", "^", "&", "*"]
    ):
        counter += 1

    if len(pw) < 8:
        bsafe = False
        print("Pw to shot")
    elif pw.startswith("#"):
        safe = False
        print("Pw can't start with '#'")
    elif pw.endswith(" "):
        safe = False
        print("Pw can't end with ' '(Blank/Space)")
    elif any(x in pw for x in ["\\", "%", ":"]):
        safe = False
        print("Pw can't contain the following symbols: \n ['\\', '%'', ':']")
    elif not any(y.isupper() for y in pw):
        safe = False
        print("Pw must contain at least one Upper case letter")
    elif not any(z.isdigit() for z in pw):
        safe = False
        print("Pw must contain at least one Number: \n (0..9)")
    # elif not any(w in pw for w in [',', '.', '!', '@', '#', '$', '_', '-', '^', '&', '*']):
    #     safe = False
    elif counter < 3:
        print(
            "Pw must contain at least three special character of `',', '.', '!', '@', '#', '$', '_', '-', '^', '&', '*'` that are not co-located (i.e `1ab@cde$#fgTE` is invalid due to `$#`.)."
        )
    else:
        safe = True

    return safe


def change_pw(**user: dict) -> str:
    """Changes the Password of a User, asked for falide login data

    Args:
        user - The user data
    """
    name = " "  # "Tom"
    pw_user = " "  # "T"
    counter = 0

    while not name in user:
        name = input(
            "Input unser Name, Tip: Hans: \nHans:\tT&e&s&t1, \nPeter:\tT&e&s&t1, \nTom:\tT, \nBen:\tT&e&s&t1\n"
        )
        print("wrong Username")

    print("Username ok")

    while not pw_user == user[name]:
        pw_user = input(
            "Input Pw: \nTip: \nHans:\tT&e&s&t1, \nPeter:\tT&e&s&t1, \nTom:\tT, \nBen:\tT&e&s&t1\n"
        )
    print("pw ok")

    new_pw = "1"  # "T&e&s&t1"
    repeat_pw = "2"  # "T&e&s&t1"
    while new_pw != repeat_pw:
        new_pw = input("Enter new Password: (Type 'cancel' to abbord)")
        if new_pw == "cancel":
            quit()
        if check_pw(new_pw):
            repeat_pw = input("Repeat the new Password:")

    user[name] = new_pw
    print("Pw Changes")
    print(user)
    return


user = {"Hans": "T&e&s&t1", "Peter": "T&e&s&t1", "Tom": "T", "Ben": "T&e&s&t1"}


change_pw(**user)

# Impressive implementation!
# tested with:
# test_pws = ["thisIs7",  # False
#             "ThisStill_isWr0ng!",  # False
#             "#violated_St4rT!",  # False
#             "Adds4N.Sp4c3_toTh3End! ",  # False
#             "Thi5_Should-w9rK!",  # True
#             "$thi5_should-not^w9rk!",  # False
#             "Thi5_n0t_Should-w9rK!!",  # False
#             "^$#@Thi5_n0t_Should-w9rK!!",  # False
#             "ch4r_not_Allo%d!",  # False
#             "ch4r_not_Allo:d!",  # Falsea
#             "ch4r_not_Allo\d!",  # False
#             "____not_All9wed!",  # False
#             "12345678!9#10A_",  # True
#             "???no_spec 4 ? Signs#should_go",  # True
#             ",t!h.s-i^s@v4L#i_D*"]   # True
#
# code fails for 
#             "$thi5_should-not^w9rk!",  # False
#             "Thi5_n0t_Should-w9rK!!",  # False
# which are the tricky ones
#
# --> 9P (7+2)

#############################################################
# 8)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 8) \n ")

from tabulate import tabulate


def print_stocks(stocks) -> None:
    """Formants a List and tabulates it in a printout

    Args:
        stocks - The list with data
    """
    print(
        tabulate(
            stocks[1:],
            headers=stocks[0],
            tablefmt="simple",
            numalign="right",
            stralign="left",
        )
    )


stocks = [
    ("Name", "Price", "Change"),
    ("AAC", 3.372, -0.8300000000002),
    ("IBC", 102.321, 52.10000000009),
    ("RF", 11.36, -3.21),
    ("PTSD", 2.17, -13.6699999999991),
    ("RG2", 819.002, -5.999999999996),
]


print_stocks(stocks)

# well importing other modules is cheating, but it wasn't explicitly excluded...
# --> 6P
