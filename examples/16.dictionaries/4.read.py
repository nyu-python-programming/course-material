def main():
    student_info_dict = {
        'name': 'Foo Barstein',
        'email': 'fb1258@nyu.edu',
        'assgn avg': 77,
        'exam 1': 89,
        'exam 2': 100,
    }

    # read a value by referencing its key
    exam1_score = student_info_dict['exam 1']
    print("The student scored {} on exam 1!".format(exam1_score))

    # read a value by referencing its key, where the key does not actually exist
    # phone_number = student_info_dict['phone'] # crash!  this produces a key error.

    # read a value by referencing its key, where the key does not actually exist
    extra_credit = student_info_dict.get('extra credit', 0)
    print("The student's has {} points of extra credit.".format(extra_credit))

    # student_info_dict[2 : 4] # there is no slicing in dictionaries!!

# call the main function
main()
