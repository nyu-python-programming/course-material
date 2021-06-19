correct_password = 'flabbergast'

def main():
    keep_going = True
    counter = 0

    # keep looping as long as the user has not guessed correctly and has not yet guessed 10 times

    while keep_going:
        # ask the user to enter the password
        attempt = input("Please enter your password: ")
        # check whether the password the user entered is correct
        if attempt == correct_password:
            keep_going = False
            print("Welcome!")
        else:
            # they made a failed attempt
            if counter < 9:
                # they have more attempts available
                print("Incorrect password.  Try again.")
            else:
                # this was their last attempt
                print("Incorrect password.")
                print("Too many failed attempts.  Bye bye.")
                keep_going = False

        counter += 1 # increment the counter

    print("Done!")


# call the main function
main()
