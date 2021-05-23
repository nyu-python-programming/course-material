# More about Dictionaries

## Dictionary functions

- `x = {0: 'first', 1: 'second'}`
- find out how many members are in a dictionary: `len(x) -> 2`
- loop through the keys in a dictionary: `for key in x.keys():`
- loop through the values in a dictionary: `for value in x.values():`
- loop through both keys and values in a dictionary: `for key,value in x.items():`
- find out if a value is being used as a key in a dictionary: `if 'pancake type' in x:`
- get a list of all the keys in a dictionary: `list( x.keys() )` # -> `[0, 1]`
- get a list of all the values in a dictionary: `list( x.values() )` # -> `['first', 'second']`
- remove a member from a dictionary: `x.pop(0)`
- add a member to a dictionary: `x['pancake type'] = 'buckwheat'`
- look up a value associated with a key: `x['pancake type']` # -> `'buckwheat'`
- another way to look up a value associated with a key: `x.get('pancake type')` # -> `'buckwheat'`
- look up a value associated with a key, but return a default value if that key is not in use: `isRealSyrup = x.get('real maple syrup', False)`
- remove all members from a dictionary: `x.clear()`
- create a copy of a dictionary: `x.copy()`
- merge two dictionaries: `x.update(y)` # where y is another dictionary

## Comprehensions (`<span>`)

- comprehensions are quick ways of doing common tasks that require loops
- they work with any sequence data type, like lists and strings

with strings:

- comprehensions work with strings: `x = 'berate'`
- simple comprehensions: `[c for c in x]`# -> `['b', 'e', 'r', 'a', 't', 'e']`
- comprehensions with modifiers: `[c.upper() for c in x]` # -> `['B', 'E', 'R', 'A', 'T', 'E']`
- comprehensions with filters: `[c for c in x if c!="e"]` # -> `['b', 'r', 'a', 't']`

same with lists:

- comprehensions work with lists: `x = [0, 1, 2, 3, 4]`
- simple comprehensions: `[c for c in x]` # -> `[0, 1, 2, 3, 4]`
- comprehensions with modifiers: `[c*2 for c in x]` # -> [`0, 2, 4, 6, 8]`comprehensions with - filters:`[c*2 for c in x if c*2<6]`# ->`[0, 2, 4]`

## Dictionary examples

### Dictionary looping

Dictionaries are basically the same as \"associative arrays\" and \"hash tables\"

```python
cat = {
   'breed' : "sphynx",
   'color' : 'grey',
   'age' : 14,
   'name' : 'fusha',
   True: "goo",
   10: 15,
   10.2: 15.9,
   'faces': ['happy', 'sad', 'grumpy']
}
```

```python
#loop through a dictionary keys
print("looping through the dictionary keys...")
for k in cat.keys():
   print(k)
```

```python
#loop through a dictionary values
print("\nllooping through the dictionary values...")
for v in cat.values():
   print(v)
```

```python
#loop through a dictionary keys and values
print("\nlooping through the dictionary keys and values...")
for k,v in cat.items():
   print(k,v, sep=" -> ")
```

```python
#find the presence of a certain value in the dictionary
print("\ndetecting whether goo is one of the values in the dictionary")
if "goo" in cat.values():
   print("Yes, goo is one of the values.")
```

```python
#find the presence of a certain value in the dictionary
print("\ndetecting whether goo is one of the values in the dictionary")
if "color" in cat.keys():
   print("Yes, color is one of the keys.")
```

### Dictionary copying

```python
#this shows you the difference between mutable data types and immutable data types
#for mutable types you get an alias with the assignment operator
#for immutable types you get a copy with the assignment operator

cat1 = {
   'breed' : "sphynx",
   'color' : 'grey',
   'age' : 14,
   'name' : 'fusha',
   True: "goo",
   10: 15,
   10.2: 15.9,
   'faces': ['happy', 'sad', 'grumpy']
}
```

```python
#create an alias of the dictionary
cat2 = cat1

# modify the cat referred to by cat1
cat1['name'] = 'bob'

#both cats point to the same dictionary in memory
print("\nShowing you that cat1 and cat2 are pointing to the same spot in memory")
print("cat1's name is " + cat1['name'])
print("cat2's name is " + cat2['name'])

#compare that to an immutable data type
cat1Name = "foo"

#make a copy of a string
cat2Name = cat1Name
cat1Name = "sherry"

print("\nShowing you that cat2Name was a copy of cat1Name")
print("cat1Name is " + cat1Name)
print("cat2Name is " + cat2Name)
```

```python
#to make a copy of an mutable data type, you need to do something different!
cat1 = cat2.copy()
cat1['name'] = 'arya'

print("\nShowing that when making a copy of a mutable data type, changing one variable does not change the data in the other")

print("cat1's name is " + cat1['name'])
print("cat2's name is " + cat2['name'])
```

## Comprehension examples

### Basic comprehension example

```python
#do a comprehension on a string
print("\nDoing a comprehension on a string...")
myString = "berate"
myList = [c for c in myString]
print(myList)
```

```python
#do the same thing without using comprehensions
print("\nDoing the same thing with a standard loop...")
myString = "negate"
myList = []
for c in myString:
    myList.append(c)
print(myList)
```

### More advanced comprehension example

```python
print("\nUse a comprehension to modify each element in a list")
list1 = ['foo', 'bar', 'goo', 'noo']
list2 = [item.upper() for item in list1]
print(list2)
```

```python
print("\nDo the same thing without comprehensions")
list1 = ['foo', 'bar', 'goo', 'noo']
list2 = []
for item in list1:
    list2.append(item.upper())
```

### Advanced comprehension example

```python
#use a comprehension to find only those elements in a list that match a certain condition
print("Using a comprehension to find elements in a list that match a certain condition...")

cats = [
    {'name': 'bob', 'color':'black'},
    {'name': 'susha', 'color':'blue'},
    {'name': 'bob', 'color':'orange'},
    {'name': 'arya', 'color':'yellow'},
    {'name': 'bob', 'color':'green'}
]

#find only those cat dictionary objects with the name key corresponding with the value 'bob'
catsNamedBob = [cat for cat in cats if cat['name']=='bob']
print(catsNamedBob)
```

```python
#do the same thing without comprehensions
print("Doing the same thing without comprehensions")

cats = [
    {'name': 'bob', 'color':'black'},
    {'name': 'susha', 'color':'blue'},
    {'name': 'bob', 'color':'orange'},
    {'name': 'arya', 'color':'yellow'},
    {'name': 'bob', 'color':'green'}
]

catsNamedBob = []

for cat in cats:
    if cat['name'] == 'bob':
        catsNamedBob.append(cat)
```
