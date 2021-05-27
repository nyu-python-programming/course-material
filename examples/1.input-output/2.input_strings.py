def main():
    """
    Solicit input from the user using the input() function and do something with that input.
    """

    name = input("Enter your name: ") # whatever the user types will be assigned to the variable, name

    message = "Welcome to the program, " + name + "!" # concatenate the three strings together and store into a varaible named message

    print(message) # print the message

# run the code called main
main()
