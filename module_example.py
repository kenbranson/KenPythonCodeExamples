def myFunction(a):
    return 2*a

# here is a function with an example of a default value for a parameter
# weirdly, default values are like module static variables.  The default is set the first time the function is called
# but if the value is changed (like adding to a list), on the next call the changed value is used because the variable
# is still there!!
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')       # raising an exception
        print complaint

# can call functions using positional arguments or by keyword
ask_ok("Are you okay?", complaint="Y/N")

# function with additional, optional args
def initlog(x, *args):
    pass    # this allows a code block which does nothing.  A non-existent code block is an error
    print(len(args))     # tells how many optional args where provided
    print(args[0])       # accesses the first optional arg

# function with additional, optional args and a dictionary input
def everything(x, *args, **dict):
    pass

args = [3, 6]    # creates a list containing (3,4,5)
name = {"a":1, "b": 2}
everything(0, *args, **name)   # Notice how to use the list and dict parameters when calling the function
