def main():

    # create a dictionary
    vegetables = [
        {
            "common name": "arugula",
            'scientific name': 'eruca vesicaria',
            "type": "leaf",
            "rich in": ['vitamin c', 'potassium']
        },
        {
            "common name": "beet",
            'scientific name': 'beta vulgaris',
            "type": "root",
            "rich in": ['manganese', 'potassium', 'iron', 'magnesium']
        },
        {
            "common name": "lettuce",
            "type": "leaf",
            "rich in": ['vitamin k', 'folate', 'beta-carotene', 'vitamin a']
        },
    ]

    # get a list of the common names of all the vegetables
    vegetable_names = [] # will hold the vegetable names
    for vegetable in vegetables:
        vegetable_names.append(vegetable['common name'])

    # keep asking the user which vegetable they would like until they don't want any more
    user_wants_more = True
    responses = [] # this will hold the vegetable names that the user wants
    while user_wants_more:
        # print out the list of vegetables
        print("\nHere are the vegetables have in stock:\n")
        for vegetable in vegetables:
            print(vegetable['common name'].capitalize())

        # validate the user's response
        keep_going = True
        while keep_going:
            response = input("Which would you like to eat? (enter 'done' when done) ")
            if response.lower() in vegetable_names:
                # the user entered a valid response
                responses.append(response)
                keep_going = False
            elif response.lower() in ['stop', 'done', 'finished', 'quit', 'go away']:
                # the user is done
                keep_going = False
                user_wants_more = False

    # print out the rich in values for the vegetable the user selected
    for vegetable in vegetables:
        if vegetable['common name'] in responses:
            # this is a vegetable the user wanted
            list_of_vegetables = ', '.join(vegetable['rich in']) # get a string with the nutrients in a comma-separated form
            # insert the word 'and' after the last comma in the list
            last_comma_index = list_of_vegetables.rfind(',')
            first_part = list_of_vegetables[:last_comma_index+1] # everything before and including the coma
            last_part = list_of_vegetables[last_comma_index+1:] # everything after the comma
            better_list_of_vegetables = first_part + ' and' + last_part

            print('Oh great, {} is rich in {}.'.format(vegetable['common name'], better_list_of_vegetables))

    print("\nEnjoy!")

# call the main functino
main()
