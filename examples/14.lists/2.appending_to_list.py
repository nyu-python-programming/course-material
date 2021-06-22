def main():

    empty_list = [] # an empty list

    empty_list.append('first value') # add a value to the end of the list
    empty_list.append('second value') # add a value to the end of the list

    # empty_list[2] = 'third value' # crash!  index out of bounds!

    empty_list.insert(1, 'third value') # inject a value at index position 1
    empty_list.insert(3, 'fourth value') # inject a value at index position 3
    empty_list.insert(20, 'fifth value') # inject a value at index position 4... not 20

    print(empty_list)


main()
