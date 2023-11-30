# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>04.py
#

### Exercise 1

# Task 1A: Implement a Python function `n_bits` that computes the bit-length of a
# nonnegative number. 
#
def n_bits(n):
    """Determines the number of bits needed to represent number `n` greater than zero
    as a binary number.

    Example
    -------
    >>> n_bits(1)
    1
    >>> n_bits(2)
    2
    >>> n_bits(3)
    2

    Parameters
    ----------
    n : integer > 0
        Decimal number whose bit-length will be determined. 

    Returns
    -------
    Returns the bit-length. 
    """
    m = 1
    M = 0
    while not (m > n):
        m *= 2
        M += 1
    return M


# Task 1B: Write a test function `test_n_bits` that compares `n_bits` with the builtin
# function `int.bit_length`
#
def test_n_bits():
    """Tests the implementation of `n_bits` by comparing it against `int.bit_length`
    for the whole numbers between 1 and 1000. 
    """
    for n in range(1, 1001):
        if n_bits(n) != int.bit_length(n):
            return False
    return True


### Exercise 2

# Implement a function `fibonacci` that produces a list of Fibonacci numbers
#
def fibonacci(n):
    """
    Returns a list of all Fibbonaci numbers equal to or smaller than a given upper
    limit. 

    Examples
    --------
    >>> fibonacci(10)
    [0, 1, 1, 2, 3, 5, 8]

    >>> fibonacci(-1)
    []

    Parameters
    ----------
    n : number (float or integer)
        Maximum number below which all Fibonacci numbers are listed. 

    Returns
    -------
    List of Fibonacci numbers (represented as integers)
    """
    a, b = 0, 1
    fibos = []
    while a <= n:
        fibos.append(a)
        a, b = b, a + b
    return fibos


### Exercise 3

# Task 3A: Implement a function `split` that splits a list into a list of lists of a
# given size
#
def split(l, size):
    """
    This function splits a list `l` into a list of sublists of a given size or smaller,
    if `len(l)` is not a multiple of `size`. 

    Examples
    --------
    >>> split([0, 1, 2, 3, 4, 5, 6, 7], 1)
    [[0], [1], [2], [3], [4], [5], [6], [7]]

    >>> split([0, 1, 2, 3, 4, 5, 6, 7], 2)
    [[0, 1], [2, 3], [4, 5], [6, 7]]

    >>> split([0, 1, 2, 3, 4, 5, 6, 7], 3)
    [[0, 1, 2], [3, 4, 5], [6, 7]]

    Parameters
    ----------
    l : list
        List that will be split into sublists of given size. 

    size : positive integer
        Desired size of sublist (if the input list is not an exact multiple of
        the desired size, the last sublist will be shorter). 

    Returns
    -------
    A list of sublists. 
    """
    return [l[start:start+size] for start in range(0, len(l), size)]


# Task 3B: Implement a function `join` that joins a list of lists into a single list
#
def join(lists):
    """
    Joins a list of lists into a single list

    Examples
    --------
    >>> join([[1, 2, 3], [3, 2], [1]])
    [1, 2, 3, 3, 2, 1]

    Parameters
    ----------
    lists : list of lists

    Returns
    -------
    A single list obtained by merging all input lists
    """
    return [elem for l in lists for elem in l]


### Exercise 4

def binom(n):
    """
    Returns the list of binomial coefficients 

       n! / (k!(n-k)!)  for k = 0, 1, ..., n 

    where k! = k * (k-1) * (k-2) * ... * 1 is the factorial of some non-negative
    integer k

    Computation of the binomial coefficients is based on Pascal's triangle:

                              1
                            1   1
                          1   2   1
                        1   3   3   1
                      1   4   6   4   1
                    1   5  10  10   5   1

    To generate the next line, we first append 1 from left and right and fill up the
    missing positions by adding pairs of neighboring numbers. 

    More details can be found here:
    * https://en.wikipedia.org/wiki/Binomial_coefficient
    * https://en.wikipedia.org/wiki/Pascal's_triangle

    Example
    -------
    >>> binom(0)
    [1]
    >>> binom(1)
    [1, 1]
    >>> binom(3)
    [1, 3, 3, 1]

    Parameters
    ----------
    n : non-negative integer
        Desired order. 

    Returns
    -------
    List of binomial coefficients
    """
    coeffs = [1]
    for _ in range(n):
        coeffs = [a + b for a, b in zip([0] + coeffs, coeffs + [0])]
    return coeffs


### Test code

def test_fibonacci():
    cases = [(10, [0, 1, 1, 2, 3, 5, 8]),
             (0, [0]),
             (1, [0, 1, 1]),
             (-1, [])]
    for inp, out in cases:
        if fibonacci(inp) != out:
            return False
    return True

    
def test_split():
    cases = [(([1, 2, 3, 4], 1), [[1], [2], [3], [4]]),
             (([1, 2, 3, 4], 2), [[1, 2], [3, 4]]),
             (([1, 2, 3, 4], 3), [[1, 2, 3], [4]]),
             (([1, 2, 3, 4], 4), [[1, 2, 3, 4]])]
    for inp, out in cases:
        if split(inp[0], inp[1]) != out:
            print('failed at:', result)
            return False    
    return True


def test_join():
    cases = [([1, 2, 3, 4], [[1], [2], [3], [4]]),
             ([1, 2, 3, 4], [[1, 2], [3, 4]]),
             ([1, 2, 3, 4], [[1, 2, 3], [4]]),
             ([1, 2, 3, 4], [[1, 2, 3, 4]])]
    for out, inp in cases:
        if join(inp) != out:
            print('failed at:', inp)
            return False    
    return True


def test_binom():
    cases = [(0, [1]),
             (1, [1, 1]),
             (2, [1, 2, 1]),
             (3, [1, 3, 3, 1]),
             (4, [1, 4, 6, 4, 1]),
             (5, [1, 5, 10, 10, 5, 1])]
    for inp, out in cases:
        if out != binom(inp):
            print('failed at:', inp)
            return False
    return True


if __name__ == '__main__':
    print('Function `n_bits` works?', test_n_bits())
    print('Function `fibonacci` works?', test_fibonacci())
    print('Function `split` works?', test_split())
    print('Function `join` works?', test_join())
    print('Function `binom` works?', test_binom())    
