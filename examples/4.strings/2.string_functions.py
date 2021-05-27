def main():
    """
    Examples of a few useful functions related to strings.
    """


    # count characters in a string
    message = "Today is Thursday!"
    num = len(message) # len() returns an int
    print('The number of characters in "' + message + '" is ' + str(num) + ".")

    # check whether the string is in title case
    message = "Today Is Thursday!"
    is_title = message.istitle()
    print('The string, "' + message + '", is in title case: ' + str(is_title) + ".")

    # check whether the string is uppercase
    message = "Today Is Thursday!"
    message = message.upper() # create an uppercase version of the string and reassign message to point to that new version
    is_upper = message.isupper()
    print('The string, "' + message + '", is in uppercase: ' + str(is_upper) + ".")

    # check whether the string is uppercase
    message = "Today Is Thursday!"
    ends_with_foo = message.endswith('foo') # determine whether or not the string ends in the text, 'foo'
    print('The string, "' + message + '", ends with "foo": ' + str(ends_with_foo) + ".")

# run the main code
main()