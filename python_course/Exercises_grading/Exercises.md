# Exercises for grading

## Setup Exercise work (1P)

- Create a new git branch from the development branch with the name "<yourName>_exercises",
please enter "yourName" that it is relatable to your real name
  - hint: you can do that from either the website (in the `python_course` click on the "Branch button",
select `development`, click the branch button again and type in the branch name, select "create from development")
or via the Jupyter (click on current branch and select "new branch") or vscode extensions.
- put all your solutions into the Exercises for grading folder
- All of the exercises are written in Mardown, so you might want to think about copying the exercise to a jupyter notebok that
has the same name as your branch
- you can then solve most of it in the notebook
- If you think it makes sense to provide a separate file, please add you as an author to the file,
i.e. `__author__ = Peter Pan` (substitute Peter Pan with your name) somewhere are the top of the file

## Slicing

1) Create a slicing that removes the last 3 items from the sequence `seq` (1P).

2) Create a slicing that selects the second half of the
sequence `seq`. Add another slicing that selects every
third element of the first half.
Half should be defined by:
first 50% end with the len(squence) // 2 element included (2P).

1) Create a slicing that selects the third and
forth element of a sequence (1P).

1) Explain the output of the following slicings for
the sequence `seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` (3P):

    1) `seq[::-1]`?
    2) `seq[6:1:-1]`
    3) `seq[:4:-1]`
    4) `seq[3::-2]`
    5) `seq[-3:1:-1]`
    6) `seq[1:4:-2]`

## Logical operators and comparisons

1) What is the result of `print("hi") or 1`? Explain the result (1P).

   
2) Explain why the following conditions are true (3P):

    - `[1, 2, 3] < [1, 2, 4]`  
           Evaluated "left" to "right", first difference `3 < 4` defines the outcome.

    - `'ABC' < 'C' < 'Pascal' < 'Python'`
           Evaluation 'left' to 'right'. `'A'< 'C' < 'Pa' < 'Py'`

    - `[1, 2, 3, 4] < [1, 2, 4]`
           Still the first difference is `3 < 4` even if the second list is shorter.

    - `[1, 2] < [1, 2, -1]`
           First difference is the length, the latter list is longer, hence, greater.

    - `[1, 2, 3] == [1.0, 2.0, 3.0]`
           integer can be compared to floats. No differnce in sequences

    - `[1, 2, ['aa', 'ab']] < [1, 2, ['abc', 'a'], 4]`
           First difference in the third element 'aa' < 'abc'

## Functions

1) Write a short function that takes a sequence and
returns the input sequence with the maximum value removed.
Name the function `remove_max_val` (2P + 1P for fulfilling python style)

2) Write a function that checks whether each element of
a sequence is true (1P + 1P for fulfilling python style guide).

3) Suppose you have a function that prints some output such as:

    ```python
    def print_spacer(text):
        print("I got this text: ", text)
    ```

    What is the return value of this function? Shortly explain (1P).

4) You have a list `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
which you would like to sort according to the rest of the integer
division of `4`. You do not want to define a new function or list
object for it. So you are looking for a solution using the
`list.sort` function (2P).
Hint: expected result is `[4, 8, 1, 5, 9, 2, 6, 10, 3, 7]`

5) Write a function that prints a spacer text around an input string.
The spacer should print a line with `"#"` characters that is as
long as the line containing the input text.
The input text should start with a `"#"` character followed by
a space character, then the input string, and as closing a space
with another `"#"` character.
The last line is the same as the first (2P + 1P for fulfilling python style guide).
Example output:

    ```python
    >> print_spacer("test")
    ########
    # test #
    ########
    ```

6) Write a function that counts the number of occurrences of a word in an input text,
not distinguishing between capitalizations, e.g. count "my" in "My example text."
results in 1 (2P + 1P for fulfilling python style guide).

7) Suppose the user needs to renew his or her password.
Write a short script that allows the input of a new password and
checking the password against requirements (no need to go full security mode,
storing plain passwords in memory is allowed.).
Use a function that checks whether password requirements are fulfilled.
The following password requirements should be enforced:

    - length of at least 8 characters
    - must not start with `'#'` or end with spaces
    - must not contain `'\'`, `'%'`, and `':'`
    - must contain at least one capital letter, at least one number `0-9`,
  and at least three special character of `',', '.', '!', '@', '#', '$', '_', '-', '^', '&', '*'`
  that are not co-located (i.e `1ab@cde$#fgTE` is invalid due to `$#`.).
  
    The function should return `true` if the requirements are fulfilled and `false` when the requirements are violated.

    The script should run as long as the requirements are not fulfilled or the user enters `'cancel'`. You can assume the requirements are known to the user, still the user needs to be reminded how to break the input script.
    Hint: you might want to develop the test function, statement for statement (8P + 2P for fulfilling python style guide).

8) Write a function, `print_stocks` that takes a
stock report extract and prints a formatted table (4P + 2P for fulfilling python style guide).
The table format should look like this:

- Table column names are centered and evenly spaced
- Header should be separated by '-' characters, with a space
indicating a column break
- all columns are evenly spaced
- string values are left aligned in a column
- numerical values are right aligned in a column

  Example:

    ```python
    stocks = [('Name', 'Price', 'Change'),
              ('AAC', 3.372, -0.8300000000002),
              ('IBC', 102.321, 52.10000000009),
              ('RF', 11.36, -3.21),
              ('PTSD', 2.17, -13.6699999999991),
              ('RG2', 819.002, -5.999999999996)]
    print_stocks(stocks)
       Name      Price      Change  
    ---------- ---------- ----------
    AAC              3.37      -0.83
    IBC            102.32      52.10
    RF              11.36      -3.21
    PTSD             2.17     -13.67
    RG2            819.00      -6.00
    ```

## Mutability, lists, and data structures

1) Explain the following behavior (3P):

    ```python
    a = [[2]] * 3
    print(a)
    a[0].append(3)
    a[1].append(5)
    a[2][0:1] = [8, 13]
    print(a)
    a[2] = [1, 2, 3]
    print(a)
    ```

    Run the code first, then explain the output lines.

2) You will sometimes see that copies are made from objects via `copy.deepcopy` from the `copy` module.
Write a small script showing that even a `deepcopy` version of an integer variable does not change
the memory address for the first 1000 integers.
Print the integer value that would show a difference or print that there was no difference found
(5P + 2P for fulfilling python style guide).

    - Hint: make a deepcopy with

      ```python
      import copy
      x = 10
      y = copy.deepcopy(x)
      ```

    - Hint: only show visual printout in case you find an unequal memory address

    - Further reading about deepcopy: [python copy module](https://docs.python.org/3/library/copy.html)

3) Execute the following code and explain the outcome. Provide a best practice to prevent this common mistake (3P).

    ```python
    def add_element(element, seq=[]):
      """Adds an element to a sequence.

      If no sequence is given to the function, create an
      empty list and insert the element.
      """
      return seq.append(element)
    
    add_element(1)
    add_element(2)
    ```

4) Why does the creation of a list from a string (or casting string to list) results in a list of
'characters' (in python: len 1 strings) and not in a list with a single string entry?
(Hint: If in doubt see documentation of `list`) (2P)

    ```python
    l = list("try")
    print(l)  # ['t', 'r', 'y']
    ```

5) Find at least three ways to create a list that starts with `0` ends with `100` and only holds even numbers. Make sure to include every even number between `0` and `100` (3P).

## Code style

Python has an official code style guide, which you should read and learn to follow, as soon as possible.
In IDEs most of the time, plug-ins will show you issues directly or even solve simple ones for you.
Still it good to know the _PEP8_ style guide and how to use whitespaces and stuff... (10P)

- Read the PEP8 documentation at [PEP8](https://peps.python.org/pep-0008/)
- Answer the following questions:
  - What _counts_ for the authors and what is considered _important_ for the PEP8 style guide?
  - What is the preferred indentation length? Can I use tabs, too?
  - What is the suggested maximum line length?
  - What is the preferred way to break long lines?
  - Where do I put imports and in which order?third party imports (numpy, pandas), and local application / library specific imports (own modules)_
  - What should never be used, except for one case, with imports?
  - What should you avoid when using inline comments?
  - How should you test your object for a `None` type? How would you test if it is not None?
  - How should you test for object types?
  - How should you test for boolean states?
  - Where should you break a line when using binary operators?
  - Give an example of hanging indentation
  - Give, in total, 5 examples that show the use of spaces when using binary operators, binary operators with different priority, assignments, slicing, arguments in functions, parentheses, brackets, braces and sequences.
