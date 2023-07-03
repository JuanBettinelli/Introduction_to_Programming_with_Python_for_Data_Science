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
    >  **Solution**
    >
    >    ```python
    >    seq[:-3]
    >    ```

2) Create a slicing that selects the second half of the
sequence `seq`. Add another slicing that selects every
third element of the first half.
Half should be defined by:
first 50% end with the len(squence) // 2 element included (2P).

    > **Solution**
    >
    >    ```python
    >    seq[len(seq) // 2:]
    >    ```
    >
    >    ```python
    >    seq[:len(seq) // 2:3]
    >    ```

3) Create a slicing that selects the third and
forth element of a sequence (1P).

    >**Solution**
    >
    >```python
    >seq[2:4]
    >```

4) Explain the output of the following slicings for
the sequence `seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` (3P):

    1) `seq[::-1]`?
    2) `seq[6:1:-1]`
    3) `seq[:4:-1]`
    4) `seq[3::-2]`
    5) `seq[-3:1:-1]`
    6) `seq[1:4:-2]`

        >**Solution**: generally, `step = -1` reverses the counting of indeces, while index position does not change. Therefore, you now have to have situations with `i>j`. Other rules still apply.
        >Outputs:
        >
        >  1) [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        >  2) [7, 6, 5, 4, 3]
        >  3) [10, 9, 8, 7, 6]
        >  4) [4, 2]
        >  5) [8, 7, 6, 5, 4, 3]
        >  6) []

## Logical operators and comparisons

1) What is the result of `print("hi") or 1`? Explain the result (1P).

    >**Solution**: 'hi' gets printed, but the result is 1, as the return value of print() is None, which is considered false.

2) Explain why the following conditions are true (3P):

    - `[1, 2, 3] < [1, 2, 4]`  
      > **Solution**:
      Evaluated "left" to "right", first difference `3 < 4` defines the outcome.

    - `'ABC' < 'C' < 'Pascal' < 'Python'`
      > **Solution**:
      Evaluation 'left' to 'right'. `'A'< 'C' < 'Pa' < 'Py'`

    - `[1, 2, 3, 4] < [1, 2, 4]`
      > **Solution**:
      Still the first difference is `3 < 4` even if the second list is shorter.

    - `[1, 2] < [1, 2, -1]`
      > **Solution**:
      First difference is the length, the latter list is longer, hence, greater.

    - `[1, 2, 3] == [1.0, 2.0, 3.0]`
      > **Solution**:
      integer can be compared to floats. No differnce in sequences

    - `[1, 2, ['aa', 'ab']] < [1, 2, ['abc', 'a'], 4]`
      > **Solution**:
      First difference in the third element 'aa' < 'abc'

## Functions

1) Write a short function that takes a sequence and
returns the input sequence with the maximum value removed.
Name the function `remove_max_val` (2P + 1P for fulfilling python style guide).

    > **Example solution**
    >
    > ```python
    > def remove_max_val(seq):
    >     """ Removes max value from a sequence
    >     Args:
    >         seq (Iterable): sequence to remove the max value
    >     """
    >     if seq:
    >         seq.remove(max(seq))
    >         return seq

2) Write a function that checks whether each element of
a sequence is true (1P + 1P for fulfilling python style guide).
    >**Solution**
    >
    >```python
    >def is_true(seq):
    >    """ test if all elements are true."""
    >    # No function needed, as python provides a built-in
    >    return all(seq)
    >```

3) Suppose you have a function that prints some output such as:

    ```python
    def print_spacer(text):
        print("I got this text: ", text)
    ```

    What is the return value of this function? Shortly explain (1P).

    > **Solution**
    >
    > `None` which you can check with
    > `_ = print_spacer("hi"); print(_)`.
    > When no `return` keyword is used within a function,
    > the default return value is `None`.

4) You have a list `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
which you would like to sort according to the rest of the integer
division of `4`. You do not want to define a new function or list
object for it. So you are looking for a solution using the
`list.sort` function (2P).
Hint: expected result is `[4, 8, 1, 5, 9, 2, 6, 10, 3, 7]`

    > **Solution**
    >
    >`my_list.sort(key=lambda x: x % 4)`

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

    > **Solution**
    >
    > ```python
    > def print_spacer(input_text: str):
    >     """ Prints a spacer out of `#` characters
    >
    >     Args:
    >         input_text: text that is wrapped with spacer
    >     """ 
    >     print((len(input_text) + 4) * "#")
    >     print("# " + input_text + " #")
    >     print((len(input_text) + 4) * "#")
    > ```

6) Write a function that counts the number of occurrences of a word in an input text,
not distinguishing between capitalizations, e.g. count "my" in "My example text."
results in 1 (2P + 1P for fulfilling python style guide).

    > **Solution**
    >
    >```python
    >def count_word(word: str, input_text: str) -> str:
    >    """ return number of occurances of a word in a string."""
    >    # use casts to str just in case of other input types
    >    lower_case_input = str(input_text).lower()
    >    lower_wo_linebreaks = lower_case_input.replace("\n", "")
    >    lower_wo_linebreaks = lower_case_input.replace(",", " ")
    >    lower_wo_linebreaks = lower_case_input.replace(".", " ")
    >    list_of_words = lower_case_input.split(" ")
    >    return list_of_words.count(str(word).lower())
    >
    > test_input = """The theory of thermodynamics is the 
    > most boring thing I have ever studied. Therefore, 
    > I prefer having the sun warm my sould in 
    > the most beautiful places there are.
    > """
    > 
    > count_word('the', test_input)
    > 4
    > ```
    >
    > Counting 'the'. Tricky here is, that there are linebreaks in
    > front of occurances and words containing 'the' as a substring.

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

    > **Solution**
    >
    > provided in valid_passwords.py

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

    > **Solution**
    >
    > ```python
    > def print_stocks(stocks: list):
    >     """ print formatted table of stock price changes"""
    >     print("{:^10} {:^10} {:^10}".format(*stocks[0]))
    >     print(f"{'-':-^10} {'-':-^10} {'-':-^10}")
    >     for name, price, change in stocks[1:]:
    >         print(f"{name:<10} {price:>10.2f} {change:>10.2f}")

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

      > **Solution**:
      >Output:
      >
      >```python
      >[[2], [2], [2]]
      >[[8, 13, 3, 5], [8, 13, 3, 5], [8, 13, 3, 5]]
      >[[8, 13, 3, 5], [8, 13, 3, 5], [1, 2, 3]]
      >```
      >
      >At the creation only one list object, with three references to it, is created. Hence, when you modify the values of the references, you change the values for all three references. In order to have separate list items, you need to make sure that you create different list items, e.g. with explicit assignments.
      >
      >```python
      >a = [[2]] * 3
      >a[1].append(3)
      >print(a)
      >a.append([1])
      >a.append([1])
      >a.append([1])
      >a[1].append(2)
      >print(a)
      >a[2] = [1, 2, 3]
      >print(a)
      >```

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

        >   **Example Solution**:
        >
        >    ```python
        >    import copy
        >
        >    for i in range(1000):
        >      i_ = copy.deepcopy(i)
        >      if id(i) != id(i_):
        >        print("Addresses differ for i=", i)
        >        break
        >    else:
        >      print("No difference found")
        >    ```

3) Execute the following code and explain the outcome. Provide a best practice to prevent this common mistake (3P).

    ```python
    def add_element(element, seq=[]):
      """Adds an element to a sequence.

      If no sequence is given to the function, create an
      empty list and insert the element.
      """
      seq.append(element)
      return seq 
    
    add_element(1)
    add_element(2)
    ```

    > **Solution**
    >
    > Output:
    >
    > ```python
    > [1]
    > [1, 2]
    > ```
    >
    > Default arguments will only be created once per session. Hence, the default empty list `[]` is created once and each call of `add_element` the same mutable list object is altered instead of newly created.
    >
    > Common best practice:
    >
    > ```python
    >  def add_element(element, seq=None):
    >      """Adds an element to a sequence.
    >
    >      If no sequence is given to the function, create an
    >      empty list and insert the element.
    >      """
    >      if seq is None:
    >          seq = []
    >      return seq.append(element)

4) Why does the creation of a list from a string (or casting string to list) results in a list of
'characters' (in python: len 1 strings) and not in a list with a single string entry?
(Hint: If in doubt see documentation of `list`) (2P)

    ```python
    l = list("try")
    print(l)  # ['t', 'r', 'y']
    ```

    > **Solution**: using the list constructor, the default behaviour is equivalent to `[x for x in iterable]` and as the string is a sequence of len 1 strings, the result is a list of characters. If you want a list with 1 string item, you need to construct it with `["try"]`.

5) Find at least three ways to create a list that starts with `0` ends with `100` and only holds even numbers. Make sure to include every even number between `0` and `100` (3P).

    > **Solutions**:
    >
    >- Without specification:
    >
    >  ```python
    >  [0, 2, 100]
    >  [0, 2] + [100]
    >  list((0, 2, 100))
    >  ```
    >
    >- With specification:
    >
    >  ```python
    >  [2*x for x in range(0, 51)]
    >  ```
    >
    >  ```python
    >  list(range(101))[::2]
    >  ```
    >
    >  ```python
    >  list(range(0, 101, 2))
    >  ```

## Code style

Python has an official code style guide, which you should read and learn to follow, as soon as possible.
In IDEs most of the time, plug-ins will show you issues directly or even solve simple ones for you.
Still it good to know the _PEP8_ style guide and how to use whitespaces and stuff... (10P)

- Read the PEP8 documentation at [PEP8](https://peps.python.org/pep-0008/)
- Answer the following questions:
  - What _counts_ for the authors and what is considered _important_ for the PEP8 style guide?
    > _Readability counts and consistency is important_
  - What is the preferred indentation length? Can I use tabs, too?
    > _4 spaces, tabs only to keep consistency, never mix (not allowed)_
  - What is the suggested maximum line length?
    > _79 for code lines, 72 for comments. If teams agree,can go up to 99 as long as comments are wrapped at 72_
  - What is the preferred way to break long lines?
    > _implicit line indentation inside of parentheses, brakets, or braces._
  - Where do I put imports and in which order?
    > _at the top of the file, after module docs before module globals. In the order of std lib imports (os, requests, sys), related third party imports (numpy, pandas), and local application / library specific imports (own modules)_
  - What should never be used, except for one case, with imports?
    > _wildcard imports_
  - What should you avoid when using inline comments?
    > _state the obvious_
  - How should you test your object for a `None` type? How would you test if it is not None?

    > - _`if myob is None`_
    > - _`if myob is not None`_

  - How should you test for object types?
    > _`if isinstance(obj1, obj2)`_
  - How should you test for boolean states?
    > _`if condition:`_
  - Where should you break a line when using binary operators?
    > _break before the operator_
  - Give an example of hanging indentation

    >```python
    >x = some_long_function(
    >  var_one, var_two,
    >  var_three, ...)
    >```

  - Give, in total, 5 examples that show the use of spaces when using binary operators, binary operators with different priority, assignments, slicing, arguments in functions, parentheses, brackets, braces and sequences.

    > - _`x[8:9] = [x**2 + (a-b)]`_
    > - _`{"key": myfunc(arg1, b=2, c=d[1+offset : 15+offset])}`_
    > - _`a = [1, 2, 4, 5]`_
    > - _`x = x*2 - 1`_
    > - _`ham[lower+offset : upper+offset]`_
