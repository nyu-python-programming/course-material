def main():
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100,
        'extra credit': 10
    }

    # values = student_info_dict.values()
    # print( type(values) )
    # print( values )

    # iterate through the values in the dictionary
    for value in student_info_dict.values():
        print(value)

# call the main function
main()

