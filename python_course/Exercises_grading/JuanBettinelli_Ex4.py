__author__ = "Juan Bettinelli"

## Mutability, lists, and data structures

##############################################################
# 1)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 1) \n ")


# Explain the following behavior (3P):
# Run the code first, then explain the output lines.
print("Ex1")

a = [[2]] * 3
print(a)
a[0].append(3)
a[1].append(5)
a[2][0:1] = [8, 13]
print(a)
a[2] = [1, 2, 3]
print(a)

print("\n**Anwser:**")
print("The script is printing in 3 sections:\n")
print(
    "In the first it's creating a list within a list with that content '2', the inner list \nis copyed 3 times creating a list  [[2], [2], [2]]\n"
)
# important: these are 3 references to the same list object
print(
    "In the second step: \nThe 1st innerlists is appended with a entery of '3', but as it is \ndeclaed that any change made to the list is tranfered to alle inner list allement it changes them all."
)
print(
    "The same is repeated with the value '5' for the  the 2nd list, and tranferd to all inner lists."
)
print(
    "Lastly the 3 innerlist is modefied so that the first index are fild with a List containing \n'[8,13]', merging the lists to form lists with 4 index, all the changes are again trenfered to all inner lists\n"
)
print(
    "In the last printing step the entire 3 inner list is replaced with the list '[1, 2, 3]'\n"
)

# clear explanations except reference vs object difference
# -->2.5P

##############################################################
# 2)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 2) \n ")

import copy

mem_diff = True
for i in range(10):
    j = copy.deepcopy(i)
    if hex(id(i)) != hex(id(j)):
        print("Different at:", i)
        mem_diff = True

print("Is the memory different in a deep copy:", mem_diff)

# --> 7P

##############################################################
# 3)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 3) \n ")


def add_element(element, seq=[]):
    """Adds an element to a sequence.

    If no sequence is given to the function, create an
    empty list and insert the element.
    """
    seq.append(element)
    return seq


print(add_element(1))
print(add_element(2))


print("Best Praxis:")
print("'.append' does not return anything, it default to None")
print(
    "to fix the problem the list 'seq' has to be returned and not the result of the funktion '.append'"
)

# --> 3P

##############################################################
# 4)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 4) \n ")

l = list("try")
print(l)

print(
    "A 'string' is a ordered sequence of characteres, A 'List' is a ordered sequence of object types."
)
print(
    "When using 'list()' every charcter is taken as an object and the order is maintained"
)

# see the iterable in the list() documentation
# --> 1P

##############################################################
# 5)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 5) \n ")

list_a = list(map(lambda x: x * 2, range(51)))
print("list_a: ", list_a)

list_b = list(range(0, 101, 2))
print("\nlist_b: ", list_b)

list_c = []
for i in range(51):
    list_c.append(i * 2)

print("\nlist_c: ", list_c)

# --> 3P