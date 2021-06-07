"""
Second version of a practice problem.
We want to create a function that solicits the user's age and print out the result.
If the user enters an invalid age, we want to output a meaningful response to that.
In this version, we use 'and' logic instead of nested 'if' statements within the `get_age()` function.
"""

def get_age():
    """
    Get the user's age as an integer

    :returns: The age, as an int
    """
    age = input("What's your age? ")
    if age.isnumeric() and int(age) <= 150:
        # the user entered a valid integer
        age = int(age)
        return age
    else:
        # the user did not enter an integer
        return None

def main():
    """
    The main logic of our program.
    """

    age = get_age() # call the function and store the return value

    # determine whether the user entered a valid age
    if age == None:
        # the user entered an invalid response
        # we know this because the return value of the function is None
        print("You entered an invalid age.  Go away!")
    else:
        # the user entered a valid response
        # print out the age of the user
        message = "The user's age is {}.".format(age)
        print(message)

# call the main function
main()