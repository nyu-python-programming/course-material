def main():

    empty_list = [] # an empty list

    list_with_some_values = ['one', 'two', 'buckle my shoe'] # a list with string values only

    list_with_a_mix_of_values = [True, False, 1, 2, 3.14, "hello", None, [1, 2, 3], { 'name': 'Foo', 'age': 42 } ] # a list with a mix of different data types

    num_values = len(list_with_a_mix_of_values) # get the length of the list
    print( 'There are {} values in the list.'.format(num_values) )


main()
