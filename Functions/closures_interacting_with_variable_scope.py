#Closures Interacting with variable scope

"""
 Pass the helper function as the key argument to a list's sort method
 The helper's return value will be used as the value for sorting each item in the list
 Checking wheter the given item is in the important group and can vary the sorting value accordingly
"""

def sort_priority(values, group):
    def helper(x):
        if x in group:
            return(0, x)
        return(1, x)
    values.sort(key=helper)

numbers = [5,54,65,8,56,1,46,3,67,46,4,79]
group = {2,3,5,7}
sort_priority(numbers, group)
print(numbers)

"""
 returning whether higher-priority items were seen
 user interface can act accordingly
 there's already a closure function for deciding which group each number is in
 closure to flip a flag the seen high-priority item
 Function can return the flag value after it's been modified by the closure
 yet the found result is False, it should be True
"""

def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found', found)

"""
when you reference a variable in a expression, the interpreter
traverses the scope to resolve the reference in this order:
"""
# -> the current function scope
# _> Any closing scopes
# +> the global scope
# => the buit-in scope

"""
assigning a value to a variable works different
if it is already defined in the current scope, just take on the new value
python treats the assignment as a variable definition
the scope of the newly defined variable is the function that contains the assignment

the assignment behavior explains the wrong return
value of the sort_priority2 function
the found variable is assigned to True in the helper closure
the closure's assignment is treated as a new variable
definition within the helper, not as assignment
within sort_priority2
"""
def sort_priority2(numbers, group):
    found = False #Scope: 'sort_priority2'
    def helper(x):
        if x in group:
            found = True #Scoper: 'helper' -- bad
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

"""
The nonlocal statement makes clear when data is being assigned
out of a closure and into another scope, complementing the global
statement and indicating that a variable's assignment should go 
directly into the module scope
"""
# do not use nonlocal beyond simple functions
# if it's getting complicated, wrap your state in a helper class

class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True

"""
closure functions can refer to variables from any of the scopes in
which they were defined
by default closures can't affext enclosing scopes by assigning
variables
use the nonlocal statement to indicate when a closure can
modify a variable in its enclosing scopes
avoid using nonlocal statements for anything beyond simple functions
