def main():
    my_list = [1, 2, 3] # create a list
    my_dict = {'second': 2, 'first': 1, 'third': 3} # create a dictionary

    value_from_list = my_list[1] # reads the second value from the list
    value_from_dict = my_dict['second'] # reads the value associated with a given key from the dictionary

    print('The second value in the list is {}.'.format(value_from_list))
    print('The value associated with the key, "second", in the dictionary is {}.'.format(value_from_dict))


# call the main function
main()
