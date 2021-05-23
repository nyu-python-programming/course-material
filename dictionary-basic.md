# Dictionaries

## Sequences refresher

- sequences contain multiple pieces of data within a single variable
- strings, lists, and ranges are all types of sequences, dictionaries
  are not
- you can access parts of a sequence using indices:
  `<span>`
- you can slice sequences:
  `<span>`
- strings hold sequences of text characters:
  `<span>`x =
  \'something\'`</font>`
- lists hold sequences of any data type:
  `<span>`x = \[None, 1,
  \"two\", 3.0, False\]`</font>`
- lists can even hold a sequence of lists:
  `<span>`x = \[ \[0, 1, 2\],
  \[\"a\", \"bad\", \"doctor\"\] \]`</font>`
- lists holding a sequence of lists are often referred to as
  multidimensional lists
- multidimensional list elements can be accessed with double indices:
  `<span>`x\[1\]\[2\] =
  \'actor\'`</font>`
- the range() function returns a sort of sequence of integers:
  `<span>`for i in
  range(10):`<span>`
- `<span>`lists
  have built-in modifier functions that \'belong\' to them:
  `<span>`
- len(x) function returns the number of elements in a sequence of any
  type
- string is immutable - you cannot just change it. You have to
  assign it to something else

```
# this will just print out lowercase foo
x = "foo"
x.upper()
print(x)
```

```
# this will print out uppercase foo
x = "foo"
x = x.upper()
print(x)
```

## Dictionary basics

- also known, in other programming languages, as a hash table or
  associative array
- are mutable, meaning you can change what\'s in after you\'ve created
  them
- similar to lists, dictionaries can be indexed:
  `<span>`
- unlike lists, dictionaries can have any immutable data type as
  indices:
  `<span>`
- (lists and dictionaries are mutable; Integers, Floats, Strings,
  Booleans, and NoneTypes are immutable; tuples are also immutable,
  but we haven\'t covered those)
- elements in a dictionary (a.k.a. members) are often referred to as
  key-\>value pairs
- the key is the index. the value is the value that the index points
  to

`<span>`\
` ``<span>`\
` ``<span>`\
` ``<span>`\
` ``<span>`\
` ``<span>`

- accessing key-\>value pairs:
  `<span>`x\[\'name\'\]
  `</font>`-\>
  `<span>`
- overwriting key-\>value pairs:
  `<span>`x\[\'age\'\] =
  13`</font>`
- creating new key-\>value pairs:
  `<span>`x\[\'gender\'\] =
  \'female\'`</font>`

## Some notable similarities and differences between dictionaries and lists

- lists require that indices be integers; dictionaries do not:
  `<span>`
- lists are sequences; dictionaries are not
- lists can be sliced; dictionaries can not
- appending to lists requires the list object\'s append() function;
  appending to dictionaries does not:
  - `<span>`x = {\'title\':
    \'On The Exactitude of Science\', \'author\': \'Jorge Luis
    Borges\'}`</font>`
  - `<span>`x\[\"year\"\] =
    1946 `<span>`\#appending a
    new member to the
    dictionary`</font>`
- like lists and other mutable types, modifying a dictionary also
  modifies any aliased variables that point to that same dictionary in
  memory:
  - `<span>`x = {0: \'first\',
    1: \'second\'}
    `<span>`\#the original
    dictionary`</font>`
  - `<span>`y = x
    `<span>`\#create a newly
    assigned variable that is an alias to the dictionary in
    memory`</font>`
  - `<span>`x\[0\] = \'the new
    first value\'
    `<span>`\#modifying the
    original
    dictionary`</font>`
  - y\[0\] now also points to \'the new first value\'

## Examples

### Basic list usage

```
#this is how you use lists...
cat = [
    'sphynx',
    'grey',
    14,
    'susha'
]

#read out the properties of the list
typeOfCat = cat[0]
ageOfCat = cat[2]
print("The " + typeOfCat + " is " + str(ageOfCat) + " old.")
```

### Basic dictionary usage

```
#this is how you use dictionaries
cat = {
    'type': 'sphynx',
    'color': 'gray',
    'age': 14,
    'name': 'susha'
}

typeOfCat = cat['type']
ageOfCat = cat['age']
print("The " + typeOfCat + " is " + str(ageOfCat) + " old.")
```

### Cat adoption system

**cat_data.py**

```
#list of cats
#each cat is a dictionary
#so this is a list that contains lots of dictionaries

cats = []
cats.append({
    'id': 100,
    'type': 'sphynx',
    'color': 'gray',
    'age': 14,
    'name': 'susha',
})
cats.append({
    'id': 8,
    'type': 'calico',
    'color': 'orange and black',
    'age': 4,
    'name': 'norman'
})
cats.append({
    'id': 29,
    'type': 'mao',
    'color': 'speckled gray',
    'age': 7,
    'name': 'arya'
})
cats.append({
    'id': 984,
    'type': 'tiger',
    'color': 'orange',
    'age': 88,
    'name': 'tony'
})
cats.append({
    'id': 7,
    'type': 'himalayan',
    'color': 'white',
    'age': 10,
    'name': 'thiksey'
})
cats.append({
    'id': 914,
    'type': 'short-haired',
    'color': 'green',
    'age': 2,
    'name': 'munchkin'
})
```

**cat_adoption_system.py**

```
#the imported file creates a list of cats
from cat_data import *

#set up a blank shopping cart that will hold the user's preferred cats to adopt
shoppingCart = []

print("Welcome to the cat adoption system. Here are our available cats:\n")

for cat in cats:
    print(cat['id'], cat['name'], cat['age'], cat['color'], cat['type'])

#keep asking the user to enter cat ids until they enter 'exit'
id = ""
while id != 'exit':

    #ask the user which cat they'd like
    id = input("\nPlease enter the id of the cat you would like to adopt (enter 'exit' to quit'): ")

    #loop through the cats and find the one with the id that the user entered
    for cat in cats:
        if str(cat['id']) == id:
            #append the selected cat to the shopping cart
            shoppingCart.append(cat)

print("Thank you for shopping at our site!")

#output all items in the shopping cart
print("You have selected the following cats to adopt:\n")

#loop through the shopping cart and output the contents
for cat in shoppingCart:
    print(cat['id'], cat['name'], cat['age'], cat['color'], cat['type'])
```

### More miscellaneous examples

```
# This one will print out 6 first characters
myfavoriteFood = "potato skins"
mySmallerFood = myFavoriteFood[0:6]
```

```
x = [
    "potatoes": "young",
    "tomatoes":"plum",
    "arugula": "baby",
    "milk": "vitamin fortified"
    ]

# loop through the items in the list
#each item comes as a key->value pair... so store them in varibles named key and variable
for k,v in x.items():
    print(k)
```

```
#List Review
shoppingList =[
    "tomatoes",
    "potatoes",
    "leeks",
    "filtered water",
    "organic grade A Vitamin AD fortified Milk"
    ]
smallerList = shoppingList [0:4]
smallerList.sort() #alphabetizing
```

```
x = {
    "potatoes": "young",
    "tomatoes": "plum",
    "arugula": "baby",
    "milk": "vitamin AD organic"
    }

for thing in x:
    print(thing) # This will print out the KEYS only
```

```
x = {
    "potatoes": "young",
    "tomatoes": "plum",
    "arugula": "baby",
    "milk": "vitamin AD organic"
    }
print(x["tomatoes"]) #this is indexing based on the keys - so this will print out "plum"
print(x.keys()) #this prints out keys only
print(x.values())#gives you values only
print(x.items())#gives you both keys and values
```

```
    x = {
        "potatoes": "young",
        "tomatoes": "plum",
        "arugula": "baby",
        "milk": "vitamin AD organic"
        }

    #loop through all the keys only
    for k in x.keys():
        print(k) #looping keys

    #loop through all the values only
    for v in x.values():
        print(v) #looping value

    #loop through all the key/value pairs
    for k,v in x.items():
        print(k,v) #looping through both


    x = {
        "potatoes": "young",
        "tomatoes": "plum",
        "arugula": "baby",
        "milk": "vitamin AD organic"
        }

    #dictionaries are mutable data types - so this updates that the arugula is old not baby
    x["arugula"] = "withered"

    #loop through all the key/value pairs
    for k,v in x.items():
        print(k,v)


    #values of any immutable data type can be a key
    x = {
        "foo": "hello",
        True: "goodbye",
        1.00: True,
        "hi": 1.2,
        None: ['a','b','c'],
        5: {'foo':'bar'}
        }

    print(x[None])



    grades = {}
    askForMore = True
    while askForMore:
        name = input("Please enter a student name: ") #key
        grade = input("What's their grade? ") #value
        grades[name] = grade
        #grades[key] = value
        another = input("Do you want to add in another student? ")
        if another.lower() == 'n' or another.lower() == "no":
            askForMore = False
    #allow the user to look up the grade that corresponds with a particular student
    name = input("Whose grade would you like to look up? ")
    print(name + "'s grade is ", grades[name])
    #if you use the same name twice, it'll give you the latest input
```
