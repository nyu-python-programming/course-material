def main():

    my_list = ['hello', 'goodbye', 'foo', 'bar', 'baz', 'bar'] # a list with 6 values

    # copy the entire list
    print(my_list[0:6]) # get a copy of the entire list
    print(my_list[0:]) # get a copy of the entire list
    print(my_list[:]) # get a copy of the entire list

    # copy the entire list in reverse
    print(my_list[5::-1])
    print(my_list[-1::-1])
    print(my_list[::-1])

    # get ['foo', 'bar', 'baz']
    print(my_list[2:5])
    print(my_list[-4:5])
    print(my_list[-4:-1])
    print(my_list[2:-1])

    # get ['baz', 'bar', 'foo']
    print(my_list[4:1:-1])
    print(my_list[-2:-5:-1])


main()
