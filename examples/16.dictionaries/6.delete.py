def main():
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100,
        'extra credit': 10
    }

    # remove a key/value pair using the pop function
    value = student_info_dict.pop('extra credit')
    print('Removed {} from the dictionary'.format(value))
    print(student_info_dict)

    # remove a key/value pair using the del keyword
    del student_info_dict['assgn avg']
    print(student_info_dict)

    # remove and return the last item added to the dictionary
    item = student_info_dict.popitem() # try not to use this one!
    print('Removed {} from the dictionary'.format(item))

    # remove all items from the dictionary with the clear function
    student_info_dict.clear()
    print(student_info_dict)



# call the main function
main()