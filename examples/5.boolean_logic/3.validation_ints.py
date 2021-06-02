def compare_ints():
    """
    A simple function that asks the user for their age, 
    converts their response to an int, and compares it to 
    a variety of other ages.
    """

    # ask for something from the user
    age = input("What is your age? ")

    # take a look at the data type.. it will always be a string because input() returns a string always
    print("The type of the string, '{}' is {}.".format(age, type(age)))

    # is what the user entered an int-looking string?
    result = age.isnumeric()
    print("The string is numeric: {}.".format(result) )

    # convert to an int
    age = int(age)

    # is this a infant
    result = age < 1
    print("You are an infant: {}.".format(result) )

    # is this a toddler (according to the CDC)
    result = age >= 1 and age <= 2
    print("You are a toddler: {}.".format(result) )

    # is this a child
    result = age < 18
    print("You are a child: {}.".format(result) )

    # is this is a teenager
    result = age >= 13 and age <= 19
    print("You are a teenager: {}.".format(result) )

    # is this is a young adult (according to WHO)
    result = age > 15 and age < 24
    print("You are a young adult: {}.".format(result) )

    # is this an adult
    result = age > 17
    print("You are an adult: {}.".format(result) )

    # is this number greater than or equal to 60
    result = age >= 60
    print("You are elderly: {}.".format(result) )

    # is this number greater than or equal to 66
    result = age > 65
    print("You are at or above retirement age: {}.".format(result) )

    # is this either a child or a retiree... give them a discount on their tickets
    result = age <= 13 or age >= 66
    print("You get a discount on your ticket: {}.".format(result))

    # is this not an adult
    result = not age > 17
    print("You are are not an adult: {}!".format(result) )

    # is this not an adult and not a teenager
    result = not age > 17 and not (age >= 13 and age <=19)
    print("You are are not an adult and not a teenager: {}!".format(result) )

    # comparing that two values are the same
    result = age == 6
    print("You are 6: {}".format(result))

    # comparing that two values are not the same
    result = age != 6
    print("You are not 6: {}".format(result))

    # comparing that two values are not the same
    result = not age == 6
    print("You are not 6: {}".format(result))

    # these three boolean expressions are equivalent
    result1 = age >= 17 and age <= 19
    result2 = 19 >= age >= 17
    result3 = 17 <= age <= 19
    same = result1 == result2 == result3
    print("The three statements result in the same value: {}".format(same))

# call the functions
compare_ints()
