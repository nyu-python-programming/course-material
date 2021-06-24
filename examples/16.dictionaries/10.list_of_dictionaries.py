def main():

    students = [
        {
            'name': 'Foo Barstein',
            'email': 'fb1258@nyu.edu',
            'assgn avg': 77,
            'exam 1': 89,
            'exam 2': 100,
            'extra credit': 10
        },
        {
            'name': 'Bar Fooburger',
            'email': 'bf1258@nyu.edu',
            'assgn avg': 55,
            'exam 1': 78,
            'exam 2': 95
        },
        {
            'name': 'Baz Barfooberg',
            'email': 'bb1258@nyu.edu',
            'assgn avg': 46,
            'exam 1': 32,
            'exam 2': 99,
            'extra credit': 2
        }
    ]
    
    for student in students:
        message = 'The student, {}, scored {} on the second exam and has {} points extra credit.'.format(student['name'], student['exam 2'], student.get('extra credit', 0))
        print(message)

# call the main function
main()
