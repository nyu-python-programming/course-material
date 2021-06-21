def main():
    
    total = 0 # an accumulator

    while total <= 21:
        num = input("Enter a number between 1 and 10: ")
        if num.isnumeric() and int(num) >= 1 and int(num) <= 10:
            total = total + int(num)
        else:
            print("Invalid number!")

    print("The total of all your numbers is: {}.".format(total))

# call the main function
main()
