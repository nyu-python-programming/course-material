def main():
    """
    A few more examples of formatting strings using the format() function, which is different from strings' .format() function!
    """

    # left-aligned, within 20 characters
    x = format('Harry', '<20s')
    print( "The string is '{}'.".format(x) )

    # right-aligned, within 20 characters
    x = format('Harry', '>20s')
    print( "The string is '{}'.".format(x) )

    # center-aligned, within 20 characters
    x = format('Harry', '^20s')
    print( "The string is '{}'.".format(x) )

    # center-aligned, within 20 characters, filled with '-' characters
    x = format('Harry', '-^20s')
    print( "The string is '{}'.".format(x) )

    # limit to two decimal places
    x = format(0.33333333, '.2f')
    print( "The string is '{}'.".format(x) )

    # limit to two decimal places, with thousands separated by commas
    x = format(3333333333.3333, ',.2f')
    print( "The string is '{}'.".format(x) )

# call the main function
main()
