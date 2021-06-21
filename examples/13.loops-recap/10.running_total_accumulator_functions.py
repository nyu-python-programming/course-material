def get_number_from_user():
    """
    Ask the user for a number, return it

    : returns : String with the user's response in it.
    """
    response = input("Enter a number between 1 and 10: ")
    return response

def is_valid_response(num):
    """
    Determines whether a given value is a number in the correct range.

    : param : num - The String that the user entered.

    : returns : True if that string is numeric and has a number in the correct range, False otherwise.
    """
    result = num.isnumeric() and int(num) >= 1 and int(num) <= 10
    return result

def report_invalid_response():
    """
    Informs the user that they entered an invalid response.
    """
    print("Invalid number!")

def output_total(total):
    """
    Print out the user's total.

    : param : total - The sum of the user's valid inputs.
    """
    print("The total of all your numbers is: {}.".format(total))

def main():
    total = 0 # an accumulator

    while total <= 21:
        num = get_number_from_user()
        if is_valid_response(num):
            total += int(num)
        else:
            report_invalid_response()

    output_total(total)

# call the main function
main()
