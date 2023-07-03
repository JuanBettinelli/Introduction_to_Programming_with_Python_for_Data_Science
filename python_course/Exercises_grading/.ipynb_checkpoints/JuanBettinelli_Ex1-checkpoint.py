__author__ = "Juan Bettinelli"

## Exesice 1 Slicing

##############################################################
# 1)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 1) \n ")

# Create a slicing that removes the last 3 items from the sequence `seq` (1P).
seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("1) ", seq[0 : (len(seq) - 3)])

##############################################################
# 2)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 2) \n ")

#Create a slicing that selects the second half of the sequence `seq`. Add another slicing that selects every third element of the first half. Half should be defined by: first 50% end with the len(squence) // 2 element included (2P).

print("The wording of this question is a bit confusing, i hope this is what was asked for.")
print("2a) ", seq[int(len(seq) / 2) : len(seq)])

print("2b) ", seq[0 : len(seq) : 3])

##############################################################
# 3)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 1) \n ")

#Create a slicing that selects the third and forth element of a sequence (1P).

print("1) ", seq[2:4])

##############################################################
# 4)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 4) \n ")

#Explain the output of the following slicings for the sequence `seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` (3P):

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1) `seq[::-1]`?
print("4.1) The comand -seq[::-1]- reverses the order of the list: \n", seq[::-1])

# 2) `seq[6:1:-1]`
print(
    "4.2) The comand -seq[6:1:-1]- reverses the order of the list, while sectioning the list. It Now starts at the 7th element and goes to the 3rd: \n",
    seq[6:1:-1],
)
# 3) `seq[:4:-1]`
print(
    "4.3) The comand -seq[:4:-1]- reverses the order of the list, while sectionent the list. It Now starts at the last element and goes to the 5th: \n",
    seq[:4:-1],
)
# 4) `seq[3::-2]`
print(
    "4.4) The comand -seq[3::-2]- reverses the order of the list and takes every second elemet, while sectionent the list. It now starts at the 4th element and goes to the first (only showing the 2nd): \n",
    seq[3::-2],
)
# 5) `seq[-3:1:-1]`
print(
    "4.5) The comand -seq[-3:1:-1]- reverses the order of the list, while sectionent the list. It now starts at the 3rd last element and goes to the 3rd : \n",
    seq[-3:1:-1],
)
# 6) `seq[1:4:-2]`
print(
    "4.6) The comand -seq[1:4:-2]- reverses the order of the list and takes every second elemet, while sectioning the list. It now starts at the 2nd element and goes to the 4th (not showing a value as the order of countig is in the oposit direktion): \n",
    seq[1:4:-2],
)
