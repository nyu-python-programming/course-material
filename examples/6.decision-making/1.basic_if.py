import random # import a module with lots of useful functions related to pseudo-random numbers

def make_random_decision():
    """
    This function generates a pseudo-random integer between 1-10 inclusive, 
    and decides whether to print something out based upon that number.
    """

    # generate a pseudo-random integer between 1-10, inclusive
    num = random.randint(1, 10)

    # show us the pseudo-random number that was generated
    print("The pseudo-random integer is {}.".format(num))

    # make a decision based upon that number
    if num < 5:
        print("It's your lucky day!")
        print("This is a beautiful message for you.")


# call the function
make_random_decision()
