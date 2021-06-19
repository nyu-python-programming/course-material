
def main():
    got_good_input = False # a flag variable!

    # a loop that stops iterating once the flag changes value
    while not got_good_input:
        # ask the user to enter valid input
        response = input("Enter a number between 1 and 10: ")
        got_good_input = response.isnumeric() and int(response) >= 1 and int(response) <= 10 # flip the flag

        if got_good_input:
            # it's good!
            print("Thank you!")
        else:
            # not a number or not in the correct range
            print("Bad number!")

    print("Done!")

# call the function
main()
