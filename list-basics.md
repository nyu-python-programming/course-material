# List basics

- create a list of
  integers:`<span>` a = \[0, 1,
  2\]`</font>`
- create a list of strings:
  `<span>`b = \[\"one\",
  \"two\", \"buckle\", \"my\",
  \"shoe\"\]`</font>`
- concatenate lists: `<span>`c =
  a + b`</font>` -\>
  `<span>`\[0, 1, 2, \'one\',
  \'two\', \'buckle\', \'my\',
  \'shoe\'\]`</font>`
- lists can hold any mixture of data
  types:`<span>` x = \[0,
  \"shoe\", True, 4.0, None\]`</font>`
- lists are sequences, like strings:
  `<span>`
  -\>
  `<span>`
- `<span>`lists
  have positive and negative indices:
  `</font>`x\[-1\] -\>
  None`</font>`
- reversing lists is like reversing strings:
  `<span>`
  -\> `<span>`\[None, 4.0, True,
  \"shoe\", 0\]`</font>`
- unlike strings, lists are mutable:
  `<span>`x\[1\] =
  \"u\"`<span>` is not an
  error!`</font>`

## List slicing

- creating a list: `<span>`x =
  \[\'c\', \'a\', \'t\'\]`</font>`
- forward slicing:
  `<span>`x\[0:2\]
  `</font>`-\>
  `<span>`\[\'c\',
  \'a\'\]`</font>`
- reverse slicing:
  `<span>`x\[-1: -3,
  -1\]`</font>`
  -\>`<span>` \[\'t\', \'a\',
  \'c\'\]`</font>`
- custom step amount:
  `<span>`x\[0:3:2\]
  `</font>`
  \[\'c\', \'t\'\] `</font>`
- automatic beginning
  index:`<span>`
  x\[:2\]`</font>` -\>
  `<span>`\[\'c\',
  \'a\'\]`</font>`
- autotomatic end index:
  `<span>`x\[1:\]
  `</font>`-\>
  `<span>`\[\'a\',
  \'t\'\]`</font>`
- automatic beginning and end indices:
  `<span>`
  -\>`<span>` \[\'c\', \'a\',
  \'t\'\]`</font>`
- shortcut for reversing a
  list:`<span>`
  x\[::-1\]`</font>` -\>
  `<span>`\[\'t\', \'a\',
  \'c\'\]`</font>`

## More list techniques

- looping through elements in a list:
  `<span>`for i in
  x:`</font>`
- checking for a needle in a haystack:
  `<span>`if i in
  x:`</font>`

## Aliases vs. copies

Know the difference between the two:

- alias
- copy

```
x = [3, 4, "lock", "the", "door"]
y = x # y and x are aliases - two variables that refer to the same memory address
z = x.copy() # z points to a copy of what x and y point to
x[2] = "open" # x and y both refer to the updated list
print(z[2]) # prints from z's copy of the original list -> "lock"
```

## More about lists

Click to read [more about lists](More_Lists), including List
functions and operations.

## Examples

### Basic list looping and slicing

```
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

```
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

```
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

They are both [Sequence data
types](https://docs.python.org/3.5/library/stdtypes.html#sequence-types-list-tuple-range),
after all.

```
 x = "this that and the other"

 for c in x:
     print(c)


 subString = x[0:10]
 print(subString)
```
