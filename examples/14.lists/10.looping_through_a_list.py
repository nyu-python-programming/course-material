def main():
    
    my_list_1 = ['hello', 'goodbye', 'foo', 'bar']

    # iterate through the values directly using a for loop
    for value in my_list_1:
        print(value)

    # iterate through the values using index numbers in a for loop
    for i in range(len(my_list_1)):
        print(my_list_1[i])

    # iterate through the values with index numbers in a while loop
    i = 0
    while i < len(my_list_1):
        print(my_list_1[i])
        i += 1

    # iterate through the values while popping them off the list in a while loop
    while len(my_list_1) > 0:
        print(my_list_1.pop(0))


main()
