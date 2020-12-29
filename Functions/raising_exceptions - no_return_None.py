# False equivalent return mistake

def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid Inputs')

# zero return can cause issues when evaluated with if statement
# any False equivalent value to indicate errors instead of only for None could be search erronealy

#solution01 -> split the return value into two tuples

def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

# callers of the function have to unpack the tuple forcing to consider the status part
#of the tuple instead of just lookng at the result of the division

success, result = careful_divide(x, y)
if not success:
    print('Invalid Inputs')

# caller can easily ignore the first part of the tuple
# use the underscore variabla name
# also error prone as returning None

_, result = careful_divide(x, y)
if not result:
    print('Invalid Inputs')


# solution2
# never return None for special cases
# raise an exception up to the caller

def  careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs')

# the caller no longer requires an condition on the return value of the function
# assuming that the return is always valid

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid Inputs')
else:
    print('Result is %.1f' % result)

# can especify the function's return value always as a float and then it will never be None
# gradual typing doesn't provide a way to indicate when exceptions are part of the
#function's interface (checked Exceptions)

def careful_divide(a: float, b: float) -> float:
    """ Divides a by b.

    Raises:
        ValueError: When the inputs cannot be divided.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid Inputs')