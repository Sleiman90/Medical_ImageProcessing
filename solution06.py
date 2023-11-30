# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>06.py
#

# useful imports
import math
import requests
import sympy

# where to find pi on the web with a precision of 1000 digits after the decimal point
URL_PI = 'http://pi2e.ch/blog/wp-content/uploads/2017/03/pi_dec_1k.txt'

# auxiliary function that can be used in 1F
def sqrt(n):
    """Returns the square root of an integer (assuming that the input is a square)."""
    assert type(n) is int, 'Expecting integer'
    return int(math.sqrt(n))

# auxiliary function to be used if you couldn't solve 2A or 2B
def pi_from_sympy(n_fractional=1000):
    """Returns pi in string representation with the desired precision."""
    return str(sympy.N(sympy.pi, n_fractional + 1))

# The following function generates a list of the first n squares using an infinite
# while loop that is eventually terminated with a break statement. 
#
def squares(n):
    """Returns a list of the first `n` squares."""
    squares = []
    counter = 0
    while True: # start infinite loop
        counter += 1
        if counter > n: # terminate loop as soon as the condition is met
            break
        squares.append(counter ** 2)
    return squares

# Please do not change the code above this line

### Exercise 1: Loops and recursion
#
# Task 1A: Generate a list of squares using a finite while loop with a suitable
# condition to terminate the loop. 
#
def squaresA(n):
    """Returns a list of the first `n` squares."""
    squares = []
    counter = 1
    while counter <= n:
        squares.append(counter ** 2)
        counter += 1
    return squares


# Task 1B: Generate a list of squares using a for loop. 
#
def squaresB(n):
    """Returns a list of the first `n` squares."""
    squares = []
    for counter in range(1, n + 1):
        squares.append(counter ** 2)
    return squares


# Task 1C: Generate a list of squares using list comprehension. 
#
def squaresC(n):
    """Returns a list of the first `n` squares."""
    return [counter**2 for counter in range(1, 1 + n)]


# Task 1D: Generate a list of squares by summing odd numbers. 
#
def squaresD(n):
    """Returns a list of the first `n` squares."""
    last_square = 0
    squares = []
    for number in range(1, 2 * n, 2):
        last_square += number
        squares.append(last_square)
    return squares


# Task 1E: Generate a list of squares recursively. 
#
def squaresE(n):
    """Returns a list of the first `n` squares."""
    return squaresE(n-1) + [n**2] if n > 0 else []


# Task 1F: Generate a list of all Pythagorean triples among the first squares. 
#
def pythagorean_triples(n):
    """Lists all Pythagorean triples among the first n squares."""
    s = squares(n)
    return [(sqrt(a), sqrt(b), sqrt(a + b)) for a in s for b in s
            if a <= b and a + b in s]


### Exercise 2

# Task 2A: Read pi from the file available here
# http://pi2e.ch/blog/wp-content/uploads/2017/03/pi_dec_1k.txt
#
def pi_from_file(filename='pi_dec_1k.txt'):
    """Reads pi from a textfile."""
    f = open(filename)
    content = f.read()
    f.close()
    return content.strip()


# Task 2B: Retrieve pi from the web using the module requests
#
def pi_from_url(url=URL_PI):
    """Retrieves pi from the web."""
    request = requests.get(url)
    return request.text


# Task 2C: Compare pi with math.pi 
# 
def test_pi(pi):
    """Checks if the input string `pi` starts with the constant `math.pi`.

    Example
    -------
    >>> test_pi('3.141592653589793')
    True
    >>> test_pi('3.1541592653589792')
    False

    Parameters
    ----------
    pi : str
        High-precision representation of pi stored as a string.

    Returns
    -------
    True if the input string shares the same initial digits with `math.pi`, and False
    otherwise. 
    """
    return pi.startswith(str(math.pi))


# Task 2D: finding peculiar patterns in pi
#   
def find_in_pi(pattern):
    """
    Find a pattern of numbers in the fractional part of pi. Returns the position of
    the pattern if it is contained in the fractional part of pi. Returns -1, otherwise.

    Example
    -------
    >>> find_in_pi('14159')
    0
    >>> find_in_pi('999999')
    761 # Feynman point
    
    Parameters
    ----------
    pattern : str
        Pattern of consecutive numbers represented as a string.

    Returns
    -------
    The lowest index in pi where the pattern is found, and -1 on failure.
    """
    # Please uncomment the following line if you could not solve 2A or 2B, otherwise
    # use your implementation
    # pi = pi_from_sympy(n_fractional=1000)
    pi = pi_from_file()
    integer_part, fractional_part = pi.split('.')
    return fractional_part.find(pattern)


# Task 2E: count digits the fractional part of a float
#
def count_digits(number):
    """Counts how often each digit occurs in the fractional part of a floating point
    number. In order to not be limited in precision, the input number is stored as a
    string.

    Example
    -------
    >>> count_digits('10.112223333')
    [0, 2, 3, 4, 0, 0, 0, 0, 0, 0]
    """
    digits = '0123456789'
    integral_part, fractional_part = number.split('.')
    return [fractional_part.count(digit) for digit in digits]


# Task 2F: print the relative frequency of each digit
#
def print_frequency(number):
    """Prints the relative frequency of how often each digit occurs in the fractional
    part of the input float number (which is assumed to be represented as a string to
    allow for arbitrary precision). 
    """
    from builtins import sum
    counts = count_digits(number)
    n_total = sum(counts)
    for digit, n in enumerate(counts):
        print(f'frequency of {digit}: {n/n_total:6.2%}')

        
# some tests      
if __name__ == '__main__':

    # Exercise 1
    for f in (squares, squaresA, squaresB, squaresC, squaresD, squaresE):
        print(f.__name__, f(10))

    print(pythagorean_triples(100))
        
    # Exercise 2        
    if test_pi(pi_from_sympy()):
        print('pi_from_sympy works')
        
    if test_pi(pi_from_file()):
        print('pi_from_file works')
        
    if test_pi(pi_from_url()):
        print('pi_from_url works')
        
    print('Feynman horizon:', find_in_pi('999999'))
    print(count_digits(pi_from_file()))

    print_frequency(pi_from_sympy(1_000_000))

