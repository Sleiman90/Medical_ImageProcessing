# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>05.py
#
from builtins import sum

### Exercise 1

# Task 1A: Write a function that takes an input list and returns a copy of the input
# list in reverse order. 
#
def reverse(alist):
    """
    Returns a copy of the input list in reverse order.

    Examples
    --------
    >>> lst = [1, 2, 3]
    >>> print(reverse(lst))
    [3, 2, 1]
    >>> print(lst)
    [1, 2, 3]

    Parameters
    ----------
    alist : list
        Input list whose elements should be reversed. 

    Returns
    -------
    A list with items in reverse order. 
    """
    assert type(alist) is list, 'expecting a list'

    return alist[::-1]
    

# Task 1B: Write a function that checks if a list is a palindrome.  
#
def is_palindromic(alist):
    """
    Checks the input list is a palindrome, i.e. if its the same in forward or
    reversed order. If the list is palindromic the return value is 'True', otherwise
    it is 'False'. 

    Examples
    --------
    >>> is_palindromic([1, 2, 1])
    True
    >>> is_palindromic([1, 2, 3, 2])
    False

    Parameters
    ----------
    alist : list
        Input list. 

    Returns
    -------
    A Boolean value indicating if input list is palindromic (True) or not (False). 
    """
    assert type(alist) is list, 'expecting a list'

    return alist == reverse(alist)


### Exercise 2

# Task 2A: Write a function that sums all even Fibonacci numbers not exceeding 200. 
#
def task2A():
    """Sum of all Fibonacci numbers that do not exceed 200."""
    return sum([2, 8, 34, 144])


# Task 2B: Write a function that generates a list of all Fibonacci numbers that do not
# exceed a given number. 
#
def fibonacci_sequence(n):
    """Generate a list of all Fibonacci numbers not exceeding `n`.
    Examples
    --------
    >>> fibonacci_sequence(0)
    []
    >>> fibonacci_sequence(1)
    [1]    
    >>> fibonacci_sequence(8)
    [1, 2, 5, 8]    
    """
    a, b = 1, 2
    f = []
    while not a > n:
        f.append(a)
        a, b = b, a + b
    return f


# Task 2C: Write a function that checks if a number is even.
#
def is_even(n):
    """Returns `True` if input is an even number, and `False` if the input is an odd
    number.
    
    Examples
    --------
    >>> is_even(10)
    True
    >>> is_even(111)
    False
    """
    return n % 2 == 0


# Task 2D: Write a function that solves problem 2 of Project Euler for an arbitrary
# upper limit. 
#
def solve_euler2(n):
    """Sum all even Fibonacci numbers not exceeding the limit `n`.

    Examples
    --------
    >>> solve_euler2(-1)
    0
    >>> solve_euler2(2)
    2
    >>> solve_euler2(10)
    10

    Parameters
    ----------
    n : integer
        Upper limit, all even Fibonacci smaller than or equal to this limit will be
        summed up. 
    
    Returns
    -------
    The sum of all even Fibonacci numbers <= n
    """
    s = 0
    for f in fibonacci_sequence(n):
        if is_even(f):
            s += f
    return s

# 2nd version using list comprehension
def solve_euler2(n):
    """Sum all even Fibonacci numbers not exceeding the limit `n`.

    Examples
    --------
    >>> solve_euler2(-1)
    0
    >>> solve_euler2(2)
    2
    >>> solve_euler2(10)
    10

    Parameters
    ----------
    n : integer
        Upper limit, all even Fibonacci smaller than or equal to this limit will be
        summed up. 
    
    Returns
    -------
    The sum of all even Fibonacci numbers <= n
    """
    return sum([f for f in fibonacci_sequence(n) if is_even(f)])


# Task 2E: Write a function that solves problem 2 of Project Euler for an arbitrary
# upper limit using the fact that only every third Fibonacci number is even. 
#
def solve_euler2b(n):
    """Sum all even Fibonacci numbers not exceeding the limit `n`.

    Examples
    --------
    >>> solve_euler2b(-1)
    0
    >>> solve_euler2b(2)
    2
    >>> solve_euler2b(10)
    10

    Parameters
    ----------
    n : integer
        Upper limit, all even Fibonacci smaller than or equal to this limit will be
        summed up. 
    
    Returns
    -------
    The sum of all even Fibonacci numbers <= n
    """
    return sum(fibonacci_sequence(n)[1::3])


def solve_euler2c(n):
    """Sum all even Fibonacci numbers not exceeding the limit `n`.

    Examples
    --------
    >>> solve_euler2(-1)
    0
    >>> solve_euler2(2)
    2
    >>> solve_euler2(10)
    10

    Parameters
    ----------
    n : integer
        Upper limit, all even Fibonacci smaller than or equal to this limit will be
        summed up. 
    
    Returns
    -------
    The sum of all even Fibonacci numbers <= n
    """
    s = 0
    a, b = 1, 2
    while not a > n:
        if is_even(a):
            s += a
        a, b = b, a + b
    return s


### Exercise 3

# Task 3A
#
def compute_frequency(wavelength):
    """
    Computes the frequency of a light wave given its wavelength in nanometers (nm).

    Examples
    --------
    >>> compute_frequency(700)
    428274940000000.0

    Parameters
    ----------
    wavelength : float or int > 0
        Wavelength in nanometers. 

    Returns
    -------
    frequency : float
        Frequency of light wave in Hz. 
    """
    assert type(wavelength) in [float, int] and wavelength > 0

    c = 299792458.0 # speed of light in m/s
    f = c / wavelength * 1e9 # frequency in Hz

    # also OK
    # f = c / (wavelength * 1e-9)

    return f
        

# Task 3B
#
def print_frequency(wavelength, unit='Hz'):
    """
    Prints the frequency of a light wave given its wavelength. The wavelength is
    assumed to be given in nanometers. An optional unit for the frequency can be
    chosen by setting the second argument (default is 'Hz', supported units are:
    'Hz', 'kHz', 'MHz', 'GHz', and 'THz').

    Examples
    --------
    >>> print_frequency(700, 'THz')
    frequency = 428.3 THz

    Parameters
    ----------
    wavelength : float or int > 0
        Wavelength in nanometers. 

    Returns
    -------
    No return value, prints frequency to standard output.
    """
    assert type(unit) is str
    assert unit in ('Hz', 'kHz', 'MHz', 'GHz', 'THz')

    units = {'Hz': 1.0, 'kHz': 1e3, 'MHz': 1e6, 'GHz': 1e9, 'THz': 1e12}
    f = compute_frequency(wavelength)
    print('frequency = {:.1f} {}'.format(f / units[unit], unit))
    

# version 2: using if-elif-else
#
def print_frequency2(wavelength, unit='Hz'):
    """
    Prints the frequency of a light wave given its wavelength. The wavelength
    is assumed to be given in nanometers. An optional unit for the frequency
    can be chosen by setting the second argument (default is 'Hz', supported
    units are: 'Hz', 'kHz', 'MHz', 'GHz', and 'THz').

    Examples
    --------
    >>> print_frequency(700, 'THz')
    frequency = 428.3 THz

    Parameters
    ----------
    wavelength : float or int > 0
        Wavelength in nanometers. 

    Returns
    -------
    No return value, prints frequency to standard output.
    """
    assert type(unit) is str
    assert unit in ('Hz', 'kHz', 'MHz', 'GHz', 'THz')
    
    f = compute_frequency(wavelength)

    output = 'frequency = {0:.1f} {unit}'
    
    if unit == 'Hz':
        print(output.format(f, unit=unit))
    elif unit == 'kHz':
        print(output.format(f * 1e-3, unit=unit))
    elif unit == 'MHz':
        print(output.format(f * 1e-6, unit=unit))
    elif unit == 'GHz':
        print(output.format(f * 1e-9, unit=unit))
    elif unit == 'THz':
        print(output.format(f * 1e-12, unit=unit))
    else:
        # shouldn't happen since we checked already...
        print('Unknown unit: {}'.format(unit))
        
### Exercise 4

def n_pages(n_digits):
    """Determines the number of pages from the number of digits used to number all
    pages of a book. The input number might actually not match the number of digits
    used to number the pages of a book, in which case the function returns -1. 
    
    Example
    -------
    >>> n_pages(31)
    20
    >>> n_pages(32)
    -1
    
    Parameters
    ----------
    n_digits : integer > 0
        Total number of digits.
        
    Returns
    -------
    Number of pages or -1 (if not a valid number of digits). 
    """
    page = 0
    n = 0
    while n < n_digits:
        page += 1
        n += len(str(page))
    if n == n_digits:
        return page
    else:
        return -1

    
# test functions
def test_reverse():
    lst = [1, 2, 3]
    if reverse(lst) != [3, 2, 1]:
        return False
    if lst != [1, 2, 3]:
        return False
    return True


def test_is_palindromic():
    return (is_palindromic([1, 2, 1]) == True) and \
      (is_palindromic([1, 2, 3, 2]) == False)


def test_fibonacci_sequence():
    return fibonacci_sequence(0) == [] and \
      fibonacci_sequence(1) == [1] and \
      fibonacci_sequence(8) == [1, 2, 3, 5, 8]    


def test_is_even():
    return is_even(10) is True and is_even(111) is False


def test_solve_euler2():
    return solve_euler2(-1) == 0 and solve_euler2(2) == 2 and solve_euler2(10) == 10


def test_solve_euler2b():
    return solve_euler2b(-1) == 0 and solve_euler2b(2) == 2 and solve_euler2b(10) == 10


def test_solve_euler2c():
    return solve_euler2c(-1) == 0 and solve_euler2c(2) == 2 and solve_euler2c(10) == 10


if __name__ == '__main__':
    # Exercise 1
    print('reverse works?', test_reverse())
    print('is_palindromic works?', test_is_palindromic())

    # Exercise 2
    # Tests
    print('fibonacci_sequence works?', test_fibonacci_sequence())
    print('is_even works?', test_is_even())
    print('solve_euler2 works?', test_solve_euler2())
    print('solve_euler2b works?', test_solve_euler2b())
    print('solve_euler2c works?', test_solve_euler2c())

    # Results
    print('Sum of even Fibonacci numbers <= 200:', task2A(), solve_euler2(200))
    print('Sum of even Fibonacci numbers <= 4 million:', solve_euler2(4_000_000),
          solve_euler2b(4_000_000), solve_euler2c(4_000_000))

    print(compute_frequency(700.), 'Hz')
    print_frequency(700.0, 'THz')

