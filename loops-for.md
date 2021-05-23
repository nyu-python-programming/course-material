# For loops

Unlike [while loops](While_loops), which are most often used to repeat the execution of a block of code an indefinite number of times, for loops are usually used to execute a block of code a fixed finite number of times. Each repetition is called an iteration.

## Iterating through a series of numbers

The following examples all repeat a print statement 6 times in order to print the numbers from 5 to 10, inclusive.

### Python example

This example uses the [range function](#Ranges_in_Python) to generate the list of values to loop through.

```python
for i in range(5,11):
    print(i)
```

### Java example

```java
for (int i = 5; i <= 10; i++) {
    System.out.println(i);
}
```

### Javascript example

```javascript
for (var i = 5; i <= 10; i++) {
  console.log(i)
}
```

### PHP example

```php
for ($i = 5; $i <= 10; $i++) {
    print($i);
}
```

## Iterating through a characters in a string

The following examples all repeat a print statement 9 times in order to print the characters in the string, \'asparagus\'.

### Python example

```python
s = "asparagus"

for c in s:
    print(c)
```

### Java example

```java
String s = "asparagus";

for (int i = 0; i < s.length(); i++) {
    char c = s.charAt(i);
    System.out.println(c);
}
```

### Javascript example

```javascript
var s = "asparagus"

for (var i = 0; i < s.length; i++) {
  var c = s.charAt(i)
  console.log(c)
}
```

### PHP example

```php
$s = "asparagus";

for ($i = 0; $i < strlen($s); $i++) {
    $c = $s{$i};
    print($c);
}
```

## Iterating through a values in a list or array

The following examples all repeat a print statement 5 times in order to
output each of the following values: \'they\', \'sailed\', \'away\',
\'in\', \'a\', \'sieve\', \'they\', \'did\'.

### Python example

```python
list_of_values = [ 'they', 'sailed', 'away', 'in', 'a', 'sieve', 'they', 'did' ]

for s in values:
    print(s)
```

### Java example

```java
String[] list_of_values = { "they", "sailed", "away", "in", "a", "sieve", "they", "did" };

for (int i = 0; i < list_of_values.length; i++) {
    System.out.println(list_of_values[i]);
}
```

Java has an \"enhanced\" for loop that can loop through elements in an
array with more [syntactic sugar](https://wikipedia.org/Syntactic_sugar):

```java
String[] list_of_values = { "in", "a", "sieve", "they", "went", "to", "sea" };

for (String value : list_of_values) {
    System.out.println(value);
}
```

### Javascript example

```javascript
var list_of_values = [
  "they",
  "sailed",
  "away",
  "in",
  "a",
  "sieve",
  "they",
  "did",
]

for (var i = 0; i < list_of_values.length; i++) {
  console.log(list_of_values[i])
}
```

### PHP example

```php
$list_of_values = array( 'they', 'sailed', 'away', 'in', 'a', 'sieve', 'they', 'did' );

for ($i = 0; $i < sizeof($list_of_values); $i++) {
    print($list_of_values[$i]);
}
```

## Ranges in Python

The built-in [range() function](http://www.pythoncentral.io/pythons-range-function-explained/) in Python automatically generates a range of integer values. This is a useful function if you want to iterate through a preset list of integers.

There are several sets of arguments you can supply to this function to
customize this list.

### Single argument

```python
range(10) #generates a range of values starting from 0 up to 9, like [0,1,2,3,4,5,6,7,8,9]
```

Example usage:

```python
for i in range(10):
    print(i)
```

### Two arguments

```python
range(3, 10) #generates a range of values starting from 3 up to 9, like [3,4,5,6,7,8,9]
```

Example usage:

```python
for i in range(3, 10):
    print(i)
```

### Three arguments

Going forwards

```python
range(20, 30, 2) #generates a range of values stepping by 2's, like [20, 22, 24, 26, 28]
```

Example usage:

```python
for i in range(20, 30, 2):
    print(i)
```

Going backwards:

```python
range(30, 20, -2) #generates a range of values from 30 down to 22, stepping down by 2's, like [30, 28, 26, 24, 22]
```

Example usage:

```python
for i in range(30, 20, -2):
    print(i)
```
