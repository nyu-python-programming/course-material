---
layout: github
title: Dictionaries
permalink: /dictionary-basics
redirect_from: /dictionary-basics.md
---

# Dictionaries

## Sequences refresher

- sequences contain multiple pieces of data within a single variable
- strings, lists, and ranges are all types of sequences, dictionaries
  are not
- you can access parts of a sequence using indices: `x[52]`
- you can slice sequences: `x[15:43]`
- strings hold sequences of text characters: `x = 'something'`
- lists hold sequences of any data type: `x = [None, 1, "two", 3.0, False]`
- lists can even hold a sequence of lists: `x = [ [0, 1, 2], ["a", "bad", "doctor"] ]`
- lists holding a sequence of lists are often referred to as multidimensional lists
- multidimensional list elements can be accessed with double indices: `x[1][2] = 'actor'`
- the range() function returns a sort of sequence of integers: `for i in range(10):'`
- lists have built-in modifier functions that \'belong\' to them: `x.reverse()`
- `len(x)` function returns the number of elements in a sequence of any type
- string is immutable -> you cannot just change it. You have to assign it to something else

```python
# this will just print out lowercase foo
x = "foo"
x.upper()
print(x)
```

```python
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
- similar to lists, dictionaries can be indexed: `x[1]`
- unlike lists, dictionaries can have any immutable data type as indices: `x['color']`
- (lists and dictionaries are mutable; Integers, Floats, Strings, Booleans, and NoneTypes are immutable; tuples are also immutable, but we haven\'t covered those)
- elements in a dictionary (a.k.a. members) are often referred to as key->value pairs
- the key is the index. the value is the value that the index points to

```python
cat = {
  'breed' : 'sphynx',
  'color' : 'grey',
  'age' : 14,
  'name' : 'susha'
}
```

- accessing key->value pairs: `x['name'] -> 'susha'`
- overwriting key->value pairs: `x['age'] = 13`
- creating new key->value pairs: `x['gender'] = 'female'`

## Some notable similarities and differences between dictionaries and lists

- lists require that indices be integers; dictionaries do not: `x[15]`
- lists are sequences; dictionaries are not
- lists can be sliced; dictionaries can not
- appending to lists requires the list object\'s append() function; appending to dictionaries does not:
  - `x = {'title': 'On The Exactitude of Science', 'author': 'Jorge Luis Borges'}`
  - `x["year"] = 1946` #appending a new member to the dictionary
- like lists and other mutable types, modifying a dictionary also modifies any aliased variables that point to that same dictionary in memory:
  - `x = {0: 'first', 1: 'second'}` #the original dictionary
  - `y = x` #create a newly assigned variable that is an alias to the dictionary in memory
  - `x[0] = 'the new first value'` #modifying the original dictionary
  - `y[0]` now also points to 'the new first value'

## Examples

### Basic list usage

```python
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

```python
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

```python
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

**cat_adoption_system.py**:

```python
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

```python
# This one will print out 6 first characters
myfavoriteFood = "potato skins"
mySmallerFood = myFavoriteFood[0:6]
```

```python
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

```python
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

```python
x = {
    "potatoes": "young",
    "tomatoes": "plum",
    "arugula": "baby",
    "milk": "vitamin AD organic"
    }

for thing in x:
    print(thing) # This will print out the KEYS only
```

```python
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

```python
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
```

```python
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
```

```python
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
```

```python
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
