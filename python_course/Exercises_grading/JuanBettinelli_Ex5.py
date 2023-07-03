__author__ = "Juan Bettinelli"

## Code style
##############################################################
# 1)
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 1) \n ")

print(
    "For the Author and article the readebility of a code is very importend, this is achived with consistensy thoughout python. this quote demonstrates this mindset well.\n 'A style guide is about consistency. Consistency with this style guide is important. Consistency within a project is more important. Consistency within one module or function is the most important.' "
)

##############################################################
# 2
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 2) \n ")

print(
    "The prefered indentation length is 4 spaces.\n Tab are ok, but dont mix tabs and spaces. \n'Spaces are the preferred indentation method.Tabs should be used solely to remain consistent with code that is already indented with tabs. Python disallows mixing tabs and spaces for indentation.'"
)

##############################################################
# 3
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 3) \n ")

print("Maximum line length: 79 characters")

##############################################################
# 4
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 4) \n ")

print("Bracke long lines with wrapping the in parentheses")

##############################################################
# 5
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 5) \n ")

print(
    "'Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.'"
)
print(
    "In the order: 1)Standard library imports. 2)Related third party imports.3) Local application/library specific imports."
)

##############################################################
# 6
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 6) \n ")

print("Wildcard imports. example: 'from <module> import *'")

# there was 1 or 2 exceptions

##############################################################
# 7
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 7) \n ")

print("Avoid with inline comments: overusing them and stating the obvious")

##############################################################
# 8
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 8) \n ")

print(
    "always test with 'is' or 'is not', never the equality operators, testing for 'not none' should be done like this: 'if x is not None'"
)

#############################################################
# 9
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 9) \n ")

print("Object types shoud be tested with 'isinstance()' ")

#############################################################
# 10
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 10) \n ")

print(
    "'Don’t compare boolean values to True or False using ==', use the boolean state directly"
)

#############################################################
# 11
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 11) \n ")

print(
    "Brake the line before the binary operators, but after the binary operator is permittet just stay consitant locally"
)

#############################################################
# 12
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 12) \n ")

print(
    "Example code for hanging indentation:\n",
    "foo = long_function_name(\n",
    "    var_one, var_two,\n",
    "    var_three, var_four)\n",
)

# example:
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)

#############################################################
# 13
print("\n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n 13) \n ")

print("Binary operators: \n a = b & c")
print("Binary operators with different priority: \n a = b*c & d*f")
print("sclicing: \n test1 = test2[1:9]")

print("Function : \ndef function(x):\n    x += 1")

print("parentheses: \n file = ('test.csv',)")

print("Brackets: \n c = (a+b) * (a-b)")

print("Brache: \n spam(ham[1])")

# ---> 10P