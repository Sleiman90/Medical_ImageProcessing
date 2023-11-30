# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>03.py
#

### Exercise 1

# Exercise 1A: Implement the function `is_divisor`
def is_divisor(a, b):
    """Checks if `b` (2nd argument) divides `a` (1st argument)."""
    return a % b == 0

# Exercise 1B: Implement the function `test_is_divisor`
def test_is_divisor():
    cases = [((10, 2), True), # 2 divides 10
             ((10, 3), False), # 3 does not divide 10
             ((2, 10), False), # 10 does not divide 2
             ]
    for inp, out in cases:
        if is_divisor(inp[0], inp[1]) != out:
            return False
    return True

# Exercise 1C: Implement the function `solve1`
def solve1():
    sum = 0
    counter = 1
    while counter < 1000:
        if is_divisor(counter, 3) or is_divisor(counter, 5):
            sum += counter
        counter += 1
    return sum

# Exercise 1D: Implement the function `test_solve1`
def test_solve1():
    return solve1() == 233168

# Exercise 1E: Implement the function `solve1b`
def solve1b(maximum):
    sum = 0
    counter = 1
    while counter < maximum:
        if is_divisor(counter, 3) or is_divisor(counter, 5):
            sum += counter
        counter += 1
    return sum

# Exercise 1F: Implement the function `test_solve1b`
def test_solve1b():
    cases = [(10, 23), (20, 78), (1000, 233168)]
    for inp, out in cases:
        if solve1b(inp) != out:
            return False
    return True

# Exercise 1G: Implement the function `solve1c`
def solve1c(maximum, factor1, factor2):
    sum = 0
    counter = 1
    while counter < maximum:
        if is_divisor(counter, factor1) or is_divisor(counter, factor2):
            sum += counter
        counter += 1
    return sum

# Exercise 1H: Implement the function `test_solve1c`
def test_solve1c():
    cases = [((10, 3, 5), 23), # problem 1, maximum 10
             ((20, 3, 5), 78), # problem 1, maximum 20
             ((1000, 3, 5), 233168), # problem 1
             ((10, 3, 6), 18), # test case 2A (previous exercises)
             ((1000, 3, 6), 166833), # problem 2A
             ((10, 3, 7), 25), # test case 2B (previous exercises)
             ((1000, 3, 7), 214216), # problem 2B
             ((10, 2, 2), 20), # test case 3A (previous exercises)
             ((20, 2, 2), 90), # problem 3A
             ((25, 2, 2), 156), # problem 3A
             ((200, 2, 2), 9900), # problem 3C
             ]
    for inp, out in cases:
        if solve1c(inp[0], inp[1], inp[2]) != out:
            return False
    return True

# Exercise 1I: Implement the function `solve1d`
def solve1c(maximum, factor1, factor2, factor3):
    sum = 0
    counter = 1
    while counter < maximum:
        if is_divisor(counter, factor1) or is_divisor(counter, factor2) \
          or is_divisor(counter, factor3):
            sum += counter
        counter += 1
    return sum

# Exercise 1J: Implement the function `test_solve1d`
def test_solve1d():
    cases = [((10, 3, 3, 5), 23), # problem 1, maximum 10
             ((20, 3, 3, 5), 78), # problem 1, maximum 20
             ((1000, 3, 3, 5), 233168), # problem 1
             ((10, 3, 3, 6), 18), # test case 2A (previous exercises)
             ((1000, 3, 3, 6), 166833), # problem 2A
             ((10, 3, 3, 7), 25), # test case 2B (previous exercises)
             ((1000, 3, 3, 7), 214216), # problem 2B
             ((10, 3, 5, 7), 30), # test case 2C (previous exercises)
             ((1000, 3, 5, 7), 271066), # problem 2C
             ((10, 2, 2, 2), 20), # test case 3A (previous exercises)
             ((20, 2, 2, 2), 90), # problem 3A
             ((25, 2, 2, 2), 156), # problem 3A
             ((200, 2, 2, 2), 9900), # problem 3C
             ]
    for inp, out in cases:
        if solve1d(inp[0], inp[1], inp[2], inp[3]) != out:
            return False
    return True

### Exercise 2: Implement and debug the function `buggy`
# original version
def buggy():
    a = 0.1
    while a != 0.2:
        a += 0.01
        print(a)

# bugfree version
def buggy():
    a = 0.1
    while a <= 0.2:
        a += 0.01
        print(a)

# bugfree version
def buggy():
    a = 0.1
    while abs(a - 0.2) > 1e-10:
        a += 0.01
        print(a)

# bugfree version
def buggy():
    import math
    a = 0.1
    while not math.isclose(a, 0.2):
        a += 0.01
        print(a)



