def get_input():
    # ask the user to enter valid input
    num = input("Enter a number between 1 and 10: ")
    return num

def input_is_valid(response):
    is_good = response.isnumeric() and int(response) >= 1 and int(response) <= 10 # flip the flag
    return is_good

def output_response(got_good_input):
    if got_good_input:
        # it's good!
        print("Thank you!")
    else:
        # not a number or not in the correct range
        print("Bad number!")

def main():
    got_good_input = False # a flag variable!

    # a loop that stops iterating once the flag changes value
    while not got_good_input:
        response = get_input() # get user input
        got_good_input = input_is_valid(response) # check whether it's valid
        output_response(got_good_input) # print out the response

    print("Done!")

# call the function
main()
