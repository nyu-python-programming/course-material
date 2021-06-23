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

    # use the list's sort function
    animals.sort() # sort the list in ascending order by default
    animals.reverse() # reverse the alphabetic order
    animals.sort(reverse=True) # sort the list in descending order
    print(animals)


# call the main function
main()
