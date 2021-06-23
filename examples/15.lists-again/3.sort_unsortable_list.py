def main():

    my_list = [
        'Chilean flamingo', # string
        True, # boolean
        2, # int
        3.14, # float
        None, # NoneType
        [1,2,3], # List
        {'foo': 'bar', 'bar': 'foo'} # Dictionary
    ]

    # use the list's sort function
    my_list.sort() # crash!  cannot sort a mix of incompatible data types
    # you would want write your own sort key function if this list is something you really wanted to be able to sort
    print(my_list)


# call the main function
main()
