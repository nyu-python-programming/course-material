# List basics

- create a list of integers: `a = [0, 1, 2]`
- create a list of strings: `b = ["one", "two", "buckle", "my", "shoe"]`
- concatenate lists: `c = a + b` # -> `[0, 1, 2, 'one', 'two', 'buckle', 'my', 'shoe']`
- lists can hold any mixture of data types: `x = [0, "shoe", True, 4.0, None]`
- lists are sequences, like strings: `x[1]` -> # `"shoe"`
- lists have positive and negative indices: `x[-1]` # -> `None`
- reversing lists is like reversing strings: `x[::-1] # -> `[None, 4.0, True, "shoe", 0]`
- unlike strings, lists are mutable: `x[1] = "u"` # is not an error!

## List slicing

- creating a list: `x = ['c', 'a', 't']`
- forward slicing: `x[0:2]` # -> `['c', 'a']`
- reverse slicing: `x[-1: -3, -1]` # -> `['t', 'a', 'c']`
- custom step amount: `x[0:3:2]` # -> `['c', 't']`
- automatic beginning index: `x[:2]` # -> `['c', 'a']`
- autotomatic end index: `x[1:]` # -> `['a', 't']`
- automatic beginning and end indices: `x[:]` # -> `['c', 'a', 't']`
- shortcut for reversing a list: `x[::-1]` # -> `['t', 'a', 'c']`

## More list techniques

- looping through elements in a list: `for i in x:`
- checking for a needle in a haystack: `if i in x:`

## Aliases vs. copies

Know the difference between the two:

- alias
- copy

```python
x = [3, 4, "lock", "the", "door"]
y = x # y and x are aliases - two variables that refer to the same memory address
z = x.copy() # z points to a copy of what x and y point to
x[2] = "open" # x and y both refer to the updated list
print(z[2]) # prints from z's copy of the original list -> "lock"
```

## More about lists

Click to read [more about lists](list-more.md), including List functions and operations.

## Examples

### Basic list looping and slicing

```python
favoriteFoods = [
    'pizza',
    'bagels',
    'poutine',
    'london broil',
    'cheeseburger',
    'ice cream',
    'spaghetti',
    'quail',
    'sushi',
    'chocolate'
]

#loop through the list using a for loop
print("Looping using for loop...")
for food in favoriteFoods:
    print(food)

#loop through the list using a while loop
print("\nLooping using while loop...")
i = 0
while i < len(favoriteFoods):
    print(favoriteFoods[i])
    i = i + 1

#slice the list
print("\nSlicing the list to get the first five elements: ")
firstFiveFavoriteFoods = favoriteFoods[0:5]
for food in firstFiveFavoriteFoods:
    print(food, end=", ")

#slice the list in reverse
print("\n\nSlicing the list in reverse: ")
lastFiveFavoriteFoods = favoriteFoods[9:4:-1]
for food in lastFiveFavoriteFoods:
    print(food, end=", ")

#slice to get the middle of the list
print("\n\nSlicing to get the middle of the list: ")
middleFavoriteFoods = favoriteFoods[3:8]
for food in middleFavoriteFoods:
    print(food, end=", ")

#copy a list
print("\n\nCopying the list using a slice: ")
copyOfMyFavoriteFoods = favoriteFoods[0:10]
print(copyOfMyFavoriteFoods)

print("\n\nCopying the list using a slice with no parameters: ")
copyOfMyFavoriteFoods = favoriteFoods[:]
print(copyOfMyFavoriteFoods)

#reverse a list
print("\n\n Reversing the list using a slice: ")
reversedListOfFavoriteFoods = favoriteFoods[::-1]
print(reversedListOfFavoriteFoods)
```

### Creating an alias of a List

```python
favoriteFoods = [
    'pizza',
    'bagels',
    'poutine',
    'london broil',
    'cheeseburger',
    'ice cream',
    'spaghetti',
    'quail',
    'sushi',
    'chocolate'
]

aliasOfFavoriteFoods = favoriteFoods

favoriteFoods[1] = "rolls"

for food in aliasFavoriteFoods:
    print(food, end=", ") #outputs the modified list including 'rolls' instead of bagels
```

### Example showing the \'in\' operator

```python
favoriteFoods = [
    'pizza',
    'bagels',
    'poutine',
    'london broil',
    'cheeseburger',
    'ice cream',
    'spaghetti',
    'quail',
    'sushi',
    'chocolate'
]

#search the list for a certain element
if "poutine" in favoriteFoods and "bagels" in favoriteFoods:
    print("Ah, yes delicious cheese curds")
```

### Strings behave like Lists in some ways

They are both [Sequence data types](https://docs.python.org/3.5/library/stdtypes.html#sequence-types-list-tuple-range), after all.

```python
x = "this that and the other"

for c in x:
    print(c)

subString = x[0:10]

print(subString)
```
