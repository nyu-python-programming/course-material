def main():
    """
    Some examples of creating variables and writing string and integer
    """

    my_favorite_number = 7 # store the int 7 into the variable, my_favorite_number
    print(my_favorite_number)

    my_favorite_word = "arugula" # store the string 'arugula' into the variable, my_favorite_word
    print(my_favorite_number)

    my_other_favorite_word = 'fortitude'
    print(my_other_favorite_word)

    my_favorite_expression = '\'Twas brillig...' # escaping the apostrophe within the string literal
    print(my_favorite_expression)

    my_favorite_expression = "'Twas brillig..." # avoiding the need to escape by using different enclosing quotes than the quote character used within the string literal
    print(my_favorite_expression)

    my_other_favorite_expression = 'Like I said, "I like pizza!"'
    print(my_other_favorite_expression)

    my_third_favorite_expression = 'Like I said, "This isn\'t the menu that I ordered!"' # escaping the inner quote so the interpreter doesn't interpret it as the end of the string literal
    print(my_third_favorite_expression)

    my_preferred_way_of_writing_complex_strings = '''I said, "This isn't the menu that I ordered!"''' # avoiding the need to escape quote characters by using ''' or """ to enclose the string literal
    print(my_preferred_way_of_writing_complex_strings)

    my_preferred_way_of_writing_complex_strings = """I said, "This isn't the menu that I ordered!\"""" # sometimes even with the three quote technique, you still need to escape some characters
    print(my_preferred_way_of_writing_complex_strings)

# run the code called main
main()
