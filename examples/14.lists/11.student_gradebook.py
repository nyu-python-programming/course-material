def collect_data():
    """
    Asks the user to enter student info.  
    
    :returns: a list with each student's info as a string in that list.
    """

    grades = [] # this will store student grades

    print("Please enter student name, email, assignment average, exam 1 score, exam 2 score...")
    print("Enter 'done' when done entering students.")

    # ask the user to enter students' info
    keep_going = True
    while keep_going:
        response = input("Student: ")
        if response.lower() == 'done':
            keep_going = False
        else:
            grades.append(response)

    print("Done!")
    # print(grades)

    return grades


def calculate_grades(grades):
    """
    Calculate the total score for each student and print it out.

    :param: grades - A list of strings, where each string contains comma-separated values about a student.
    """
    # print out the total score for each student
    for student in grades:
        data = student.split(',') # get a list of this student's data
        # extract the important bits of data from this student's list
        name = data[0].strip().title()
        email = data[1].strip()
        assgn_avg = int(data[2].strip())
        exam_1 = int(data[3].strip())
        exam_2 = int(data[4].strip())

        # calculate total score
        total = assgn_avg * 0.4 + exam_1 * 0.3 + exam_2 * 0.3 
        print("{} scored {} in the class.".format(name, total))

def main():
    data = collect_data() # ask the user to enter grade info
    calculate_grades(data) # print out the total score for each student

# call the main function
main()
