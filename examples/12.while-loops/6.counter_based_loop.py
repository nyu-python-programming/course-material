def main():
    shopping_list = ['arugula', 'sorrel', 'kale', 'rhubarb', 'collard greens', 'bok choy']

    # iterate through this list of bitter greens
    i = 0 # star the index at zeo

    # iterate as many times as there are values in the list
    while i < len(shopping_list):
        # print out the value from the list at the current index position
        print( shopping_list[i] )
        i += 1 # increment the index

    print("Done!")

# run the function
main()
