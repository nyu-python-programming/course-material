def main():
    """
    A few examples of formatting strings.
    """

    # insert a variable into a string the old fashioned way
    word = "and"
    phrase1 = "Hello " + word + " goodbye."
    print(phrase1)

    # do the same thing, but use the .format() function
    phrase2 = "Hello {} goodbye.".format("and")
    print(phrase2)

    # do the same thing, but use the .format() function
    phrase3 = "{} and {}.".format("Hello", "goodbye")
    print(phrase3)

    # do the same thing, but use the .format() function with labeled placeholders
    phrase4 = "{word1} and {word2}.".format(word2="goodbye", word1="Hello")
    print(phrase4)

    # verify that these are all the same text
    is_same = phrase1 == phrase2 == phrase3 == phrase4
    is_same = str(is_same)
    result = "These are all the same string: {}.".format(is_same)
    print(result)


# run the code in the main function
main()
