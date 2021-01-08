'''
Accepting a variable number of positional arguments can make a 
function call clear and reduce visual noise
Positional arguments are called varargs or star args (*args)

'''

def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('My numbers are', [27, 72])
log('Hi there', [])

'''
passing an empty list with no values to log is noisy
prefix the last positional parameter name with *
the first parameter is required, the subsequent number
of positional arguments not
the body doesn't change, only the callers
'''
def log(message, *values):    # the * here is the difference
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('My numbers are', [27, 72])
log('Hi there') # no empty list