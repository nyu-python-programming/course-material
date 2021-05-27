def main():
    """
    Examples of how to print text to the command line using the print() function.
    """

    message1 = "Hello, welcome to this class on Tuesday!"
    print(message1) # notice that a line break is printed by default at the end of the sentence

    message2 = "Hello," # notice that there is no space after the comma
    message3 = "welcome to this class on Tuesday!"
    print(message2, message3) # notice that a space is added after message2 and a line break is printed at the end by default

    message4 = "Hello, " # notice that there IS a space after the comma
    message5 = "welcome to this class on Tuesday!"
    print(message4, message5, sep='') # notice that we override the default separator and that a line break is printed by default

    message6 = "Hello, " # notice that there IS a space after the comma
    message7 = "welcome to this class on Tuesday"
    print(message6, message7, sep='', end='!\n') # notice the exclamation and the line break added at the end

# run the code called main
main()
