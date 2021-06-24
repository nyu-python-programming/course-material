def main():
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100,
        'extra credit': 10
    }

    # keys = student_info_dict.keys()
    # print( type(keys) )
    # print( keys )

    # iterate through the keys in the dictionary
    for key in student_info_dict.keys():
        print(key)

# call the main function
main()

