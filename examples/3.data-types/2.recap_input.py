def main():
    """
    Some examples of soliciting input from the user and doing data type conversions.
    """

    num = input('Enter your favorite number: ') # input always returns a string

    new_num = num * 10 # using the * operator on a string concatenates the values
    print(new_num)

    new_num = int(num) * 10 # using the * operator on a numeric type does numeric multiplication
    print(new_num)

    new_num = float(num) * 10 # using the * operator on a numeric type does numeric multiplication
    print(new_num)

# run the code called main
main()
