def main():
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100,
        'extra credit': 10
    }

    # items = student_info_dict.items()
    # print( type(items) )
    # print( items )

    # iterate through the items in the dictionary
    print('\nPrinting out the items in their entirety...')
    for item in student_info_dict.items():
        print(item) # each item is a tuple containing the key and value

    # iterate through the items in the dictionary
    print('\nPrinting out the keys and values seperately...')
    for item in student_info_dict.items():
        key = item[0]
        value = item[1]
        print(key, value, sep=': ') # each item is a tuple containing the key and value

    # iterate through the items in the dictionary
    print('\nPrinting out the keys and values seperately...')
    for key, value in student_info_dict.items():
        print(key, value, sep=': ') # each item is a tuple containing the key and value


# call the main function
main()

