def main():


    students = [
        # name              email             assgn exam1   exam2
        ['Foo Barstein',    'fb1258@nyu.edu', 89,   72,     84],
        ['Bar Fooburger',   'bf1258@nyu.edu', 42,   44,     60],
        ['Baz Bumstein',    'bb1258@nyu.edu', 73,   69,     56],
    ]

    got_something_good = False
    while not got_something_good:
        score_type = input("Which score would you like to see? (e.g. assgn, exam1, exam2) ")

        # validate the user's input
        if score_type in ['assgn', 'exam1', 'exam2']:
            got_something_good = True
        
        # determine the index position of the value we're interested in
        if score_type == 'assgn':
            score_index = 2
        elif score_type == 'exam1':
            score_index = 3
        elif score_type == 'exam2':
            score_index = 4
        

    # iterate through all students and print out their exam 1 scores
    for student in students:
        score = student[score_index]
        message = "{} scored {} on {}.".format(student[0], score, score_type)
        print(message)

# call the main function
main()
