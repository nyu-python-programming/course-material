def do_something1():
    """
    Set the local variable x to 10 and print it out.
    """
    x = 10
    print(x) # print out the value of the local variable x


def do_something2():
    """
    Set the local variable x to 20 and print it out.
    """
    x = 20
    print(x) # print out the value of the local variable x


# set the global variable x to 0
x = 0

# call the two functions
do_something1()
do_something2()

# print out the value of the global variable x
print(x)
