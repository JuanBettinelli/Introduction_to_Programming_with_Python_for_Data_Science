"""Module holding some fibonacci calculation functions"""

def print_fib_series(max_num: int) -> None:
    """Print a Fibonacci series up to max_num.
    
    Args:
        max_num - number up to which the Fibonacci series is printed.
    """
    # Start conditions
    a, b = 0, 1
    while a < max_num:
        print(a, end=' ')
        a, b = b, a+b

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
