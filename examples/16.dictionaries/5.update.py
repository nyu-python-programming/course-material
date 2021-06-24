def main():
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100,
        'extra credit': 10
    }

    # print the student's assignment average value
    print("The student's assignment average is {}.".format(student_info_dict['assgn avg']))

    # update one of the values in the dictionary
    student_info_dict['assgn avg'] = 99

    # print the student's assignment average value
    print("The student's assignment average is {}.".format(student_info_dict['assgn avg']))



# call the main function
main()