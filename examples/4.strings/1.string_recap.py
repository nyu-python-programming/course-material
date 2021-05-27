def main():
    """
    Some simple examples of string concatenation and using the len() function.
    """

    # a string with a line break character in the middle, using the \n escape character
    message1 = 'Hello\nworld!'
    #print(message)
    num = len(message1)
    print('The number of characters in "' + message1 + '" is ' + str(num) + ".")

    # a string with a line break character in the middle, using the more natural Enter key
    message2 = '''Hello
    world!'''
    #print(message)
    num = len(message2)
    print('The number of characters in "' + message2 + '" is ' + str(num) + ".")

    # compare message1 and message2 to one another, to give a boolean value, True if they are the same, False otherwise
    is_same = message1 == message2
    print(is_same)

# run the code in the main function
main()
