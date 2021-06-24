def list_example():
    # imagine a student's info is stored in a list
    student_info_list = [
        'Foo Barstein', # name
        'fb1258@nyu.edu', # email
        77, # assignment average
        89, # exam 1
        100 # exam 2
    ]

    # access the student's exam 1 score
    exam1_score = student_info_list[3]
    print("The student scored {} on exam 1!".format(exam1_score))

def dict_example():
    # imagine a student's info is stored in a dictionary
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100
    }

    # access the student's exam 1 score
    exam1_score = student_info_dict['exam 1']
    print("The student scored {} on exam 1!".format(exam1_score))

def main():
    list_example()
    dict_example()


# call the main function
main()
