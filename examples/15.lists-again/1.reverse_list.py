def main():

    animals = [
        'Chilean flamingo',
        'Emerald-spotted wood dove',
        'Common seal',
        'Horned puffin',
        'Numbat',
        'Spotted hyena',
        'Anteater, giant',
        'Green vine snake',
        'African wild dog',
        'Quail, gambel\'s'
    ]

    # do a reverse slice
    animals[::-1] # a list slice always creates a new list in memory, so it would need to be reassigned to the animals variable, if that's what you wanted.
    print(animals)
    
    # use the list's reverse function
    animals.reverse() # the list reverse() function modifies the same list that animals refers to, therefore it does not need to be reassigned to the animals variable
    print(animals)


# call the main function
main()
