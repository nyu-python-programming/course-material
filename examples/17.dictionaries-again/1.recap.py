def main():

    # create a dictionary
    vegetable1 = {
        "common name": "arugula",
        "type": "leaf",
        "rich in": ['vitamin c', 'potassium']
    }

    # add a new key/value pair
    vegetable1['flavor'] = "bitter with a bit of mustard thrown in"

    # modify a value
    vegetable1['type'] = 'green'
    vegetable1['rich in'].append('flavor')

    # delete a value
    vegetable1.pop('flavor')

    # read a value
    message = 'The value corresponding to the key type is {}.'.format(vegetable1['type'])
    print(message)

    # iterate through the keys in the dictionary
    print('\nPrinting out the keys...')
    for key in vegetable1.keys():
        print('There is a "{}" key in the dictionary with the value "{}".'.format(key, vegetable1[key]))

    # iterate through the values in the dictionary
    print('\nPrinting out the values...')
    for val in vegetable1.values():
        print("There is a '{}' value in the dictionary.".format(val))

    # iterate through the items in the dictionary
    print('\nPrinting out the items...')
    for item in vegetable1.items():
        print('There is a {} item in the dictionary with the key "{}" and the value "{}".'.format(item, item[0], item[1]))

    # iterate through the items in the dictionary, and destructure into two separate variables
    print('\nPrinting out the items with destructuring...')
    for key, val in vegetable1.items():
        print('There is a ("{}", "{}") item in the dictionary with the key "{}" and the value "{}".'.format(key, val, key, val))

# call the main function
main()
