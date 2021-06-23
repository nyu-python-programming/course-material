def main():

    my_list = [
        'hello',
        'world',
        'goodbye',
        ['a', 'b', 'c'] # a list within a list!
    ]

    print(my_list[1]) # prints out 'world\n'

    print(my_list[3]) # prints out "['a', 'b', 'c']\n"

    print(my_list[3][1]) # prints out 'b'

# call the function
main()
