def compare_strings():
    """
    A simple function that asks the user for their name, 
    normalizes their response, and compares it to the name, 
    'Bob' in a case-insensitive manner.
    """
    
    # ask for something from the user
    name = input("What's your name? ")

    # remove any leading or trailing whitespace
    name = name.strip()

    # do case-insensitive match by removing uppercase
    name = name.lower()

    # compare to lowercase 'bob', since we converted name to lowercase
    result = name == 'bob'
    print( "Your name is Bob: {}.".format(result) )

    # is the name not Bob?
    result = name != 'bob'
    print( "Your name is not Bob: {}.".format(result) )

# call the function
compare_strings()
