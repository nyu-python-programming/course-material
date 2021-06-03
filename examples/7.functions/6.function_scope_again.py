# within a function defininition, it is possible to refer to variables defined within the global memory space.
# however, this is bad style and should be avoided! 

def do_something1():
    """
    Print out x.
    """
    print(x) # print out the value of the local variable x


def do_something2():
    """
    Print out x.
    """
    print(x) # print out the value of the local variable x


# set the global variable x to 0
x = 0

# call the two functions
do_something1()
do_something2()

# print out the value of the global variable x
print(x)
