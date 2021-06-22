def main():
    
    my_list_1 = ['hello', 'goodbye', 'foo', 'bar']
    my_list_2 = my_list_1 # make aliases!

    # modify a value in the original list
    my_list_1[2] = 'goo'

    # check what's in the copy
    print(my_list_2)

main()
