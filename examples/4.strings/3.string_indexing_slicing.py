def main():
    """
    Examples of indexing individual characters and slicing subsets of characters within a string.
    """

    my_string = "Twas brillig and the slithy toves..."

    num = len(my_string)
    print("The string has " + str(num) + " characters in it!")

    # extract a single character from the string, using an index
    print("The fourth character in the string is '" + my_string[3] + "'." )

    # extract a slice of the string, using indices
    print("The fourth thru sixth characters in the string are '" + my_string[3:6] + "'." )

    # extract a single character from the string, using a negative index
    print("The fourth-from-last character in the string is '" + my_string[-4] + "'." )
    
    # extract a slice of the string, using negative indices
    print("The fourth-from-last thru second-from-last characters in the string are '" + my_string[-4:-1] + "'." )

    # get a slice that is the entire string, from beginning to end
    print("A slice that represents the entire string is '" + my_string[:] + "'." )

    # get a slice that shows every other character, from beginning to end
    print("Every other character in the string: '" + my_string[::2] + "'." )

    # get a slice of the entire string in reverse
    print("The entire string, in reverse: '" + my_string[::-1] + "'.")

    # get a slice of the string in reverse
    print("A substring, in reverse: '" + my_string[15:4:-1] + "'.")

    # get a slice of the string, in the forwards direction
    print("A substring, in the forwards step: '" + my_string[5:16:1] + "'.")


# call the function, main
main()
