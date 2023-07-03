__author__ = "Juan Bettinelli"

## Excercice 2 Logical operators and comparisons

##############################################################
# 1)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 1) \n ")

# What is the result of `print("hi") or 1`? Explain the result (1P).

print(
    "1) It prints the Word 'hi' the 'or' operater is reduntent in this situation. \n The 'or' evaluades the first value and prits the true dirctly without looking at the 1"
)

print("hi") or 1

# did you run asign the condition and test your statement?
test = print("hi") or 1
print("test: ", test)

# --> 0P

##############################################################
# 2)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 2) \n ")

# Explain why the following conditions are true (3P):
# a) [1, 2, 3] < [1, 2, 4]  Evaluated "left" to "right", first difference `3 < 4` defines the outcome.
print(
    "2a) It evaluates from left to right the first differens in the list ist '3>4' which returns a 'true'"
)
print([1, 2, 3] < [1, 2, 4])

# b) 'ABC' < 'C' < 'Pascal' < 'Python' Evaluation 'left' to 'right'. `'A'< 'C' < 'Pa' < 'Py'`
print(
    "2b) It evaluates from lest to right, first it looks at a>c which ist 'True',\n then it looks at 'c<p' which is is also 'true', \n it looks at the next difference in 'Pa<Py' whitch is also 'true', \n hence final result is 'true' "
)
print("ABC" < "C" < "Pascal" < "Python")

# c) `[1, 2, 3, 4] < [1, 2, 4]` Still the first difference is `3 < 4` even if the second list is shorter.
print(
    "2c) It evaluates list element by element, \n the first two elements are equal, \n the third is different '3<4', this results in a 'true',\n hence the final result is 'true'"
)
print([1, 2, 3, 4] < [1, 2, 4])

# d) [1, 2] < [1, 2, -1] First difference is the length, the latter list is longer, hence, greater.
print(
    "2d) The first two elements in the two list are equal, the first difference that the seen i the length of the lists,\n as the second is lager than the first the result is 'true' "
)
print([1, 2] < [1, 2, -1])

# e) [1, 2, 3] == [1.0, 2.0, 3.0] integer can be compared to floats. No differnce in sequences
print(
    "2e) There is no difference between the integer and the Float, so the comand returns a 'true'"
)
print([1, 2, 3] == [1.0, 2.0, 3.0])

# f) [1, 2, ['aa', 'ab']] < [1, 2, ['abc', 'a'], 4] First difference in the third element 'aa' < 'abc'
print(
    "2f) The fist two entereis in the lists are the same, \n the difference is in the first element in the lists within the list. \n here the difference is 'aa<>abc' hence the result is 'false'."
)
print([1, 2, ["aa", "ab"]] < [1, 2, ["abc", "a"], 4])
