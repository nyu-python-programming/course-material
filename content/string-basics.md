---
layout: github
title: String Basics
permalink: /string-basics
redirect_from: /string-basics.md
---

# String basics

String is a data type used to store text. A String data type is built
into most high-level programming languages, since storing and
manipulating text is such a common need in programs.

## Defining strings

Each of the following examples creates a new String with the text, bla
bla bla stored in it:

### Python example

Single quotes, double quotes, triple single quotes, triple double
quotes\... it\'s all good in Python.

```
 'bla bla bla'
```

```
 "bla bla bla"
```

```
 '''bla bla bla'''
```

```
 """bla bla bla"""
```

### Java example

Double quotes must be used to define String literals in Java

```java
 "bla bla bla"
```

### Javascript example

Single quotes and double quotes are equivalent in Javascript.

```javascript
"bla bla bla"
```

```
 "bla bla bla"
```

### PHP example

Single quotes and double quotes are equivalent in PHP.

```php
 'bla bla bla'
```

```php
 "bla bla bla"
```

## Concatenating strings

Each of the following examples creates a new String with the text, bla
bla bla stored in it:

### Python example

```python
 'bla' + ' ' + 'bla' + ' ' + 'bla'
```

Note that Python also supports the \'multiplication\' operator:

```python
 'bla ' * 3
```

### Java example

```java
 "bla" + " " + "bla" + " " + "bla"
```

### Javascript example

```javascript
"bla" + " " + "bla" + " " + "bla"
```

### PHP example

```php
 'bla' . ' ' . 'bla' . ' ' . 'bla'
```

## Calculating the length of a string

The following examples show how to determine how many characters are in
a given string.

### Python example

```python
 len('bla bla bla')
```

### Java example

```java
 "bla bla bla".length()
```

### Javascript example

```javascript
"bla bla bla".length
```

### PHP example

```php
 strlen('bla bla bla')
```

## String escape characters

All high-level programming languages support escape characters in
Strings - these are written with more than one character, but actually
represent single characters in how a string is interpreted.

Common escape characters:

- `\n` -- a newline (linefeed) character
- `\r` -- a return (carriage return) character
- `\t` -- a tab character
- `\'` -- a single quote character
- `\"` -- a double quote character
- `\\` -- a backslash character

The following string represents the words hello and world, separated by
a line break:

```python
 "hello\nworld"
```

## String indexing

All high-level programming languages allow individual characters within
a String to be accessed. The following examples all access the first
fourth character (the \'r\') in the string \'fabrication\'. Note that
index numbers always start from zero.

### Python example

```python
 'fabrication'[3]
```

Python also supports negative indices

```python
 'fabrication'[-8]
```

### Java example

```java
 "fabrication".charAt(3)
```

### Javascript example

```javascript
"fabrication".charAt(3)
```

### PHP example

```php
 'fabrication'{3}
```

## Looping through characters in a string

All high-level languages allow easy looping through the individual
characters in a string.

### Python example

Forwards:

```python
 s = 'fabrication'
 for c in s:
     print(c)
```

Backwards:

```python
 s = 'fabrication'
 for c in s[::-1]:
     print(c)
```

### Java example

Forwards:

```java
 String s = "fabrication";
 for (int i = 0; i < s.length(); i++){
     char c = s.charAt(i);
     System.out.println(c);
```

Backwards:

```java
 String s = "fabrication";
 for (int i = s.length() - 1; i >= 0; i--){
     char c = s.charAt(i);
     System.out.println(c);
```

### Javascript example

Forwards:

```javascript
 var s = "fabrication";
 for (var i = 0; i < s.length; i++){
     var c = s.charAt(i);
     console.log(c);
```

Backwards:

```javascript
 var s = "fabrication";
 for (var i = s.length - 1; i >= 0; i--){
     var c = s.charAt(i);
     console.log(c);
```

### PHP example

Forwards:

```php
 $s = 'fabrication';
 for($i=0; $i < strlen($s); $i++)  {
     $c = $s[$i];
     print($c);
 }
```

Backwards:

```php
 $s = 'fabrication';
 for($i = strlen($s) - 1; $i >= 0; $i--)  {
     $c = $s[$i];
     print($c);
 }
```

## Strings are immutable

In most high-level languages, strings are immutable, meaning they cannot
be modified after being created.

### Python example

```python
 s = 'fabrication'
 s[1] = 'o' #this is an error
```

### Java example

```java
 String s = "fabrication";
 s.charAt(1) = 'o'; //this is an error
```

### Javascript example

```javascript
var s = "fabrication"
s[1] = "o" //this is an error
```

### PHP example

```php
 $s = 'fabrication';
 $s{1} = 'o'; //this is not an error, but has not changed the original string, but rather the variable $s now points to a new string with an 'o' as the second character
```

## Substrings and slicing

It is possible, in all high-level programming languages, to get a
substring, or slice, of a string. All the examples below create a new
string holding the text, \"bric\".

### Python example

```python
s1 = 'fabrication'
s2 = s1[2:6]
```

Python also supports negative indices:

```python
s1 = 'fabrication'
s2 = s1[-9:-5]
```

### Java example

```java
String s1 = "fabrication";
String s2 = s1.substring(2, 6);
```

### Javascript example

```javascript
var s1 = "fabrication"
var s2 = s1.substring(2, 6)
```

### PHP example

```php
$s1 = 'fabrication';
$s2 = substr($s1, 2, 4);
```

PHP also supports negative indices:

```php
$s1 = 'fabrication';
$s2 = substr($s1, -9, 4);
```

## Comparing the values of two strings

All high-level programming languages provide a means to determine
whether two strings hold the same text or not. The following expressions
all evaluate to a boolean false value, since \'lipsmacking\' is not the
same as \'fingerlicking\'.

### Python example

```python
'lipsmacking' == 'fingerlicking'
```

### Java example

```java
"lipsmacking".equals("fingerlicking")
```

### Javascript example

```javascript
"lipsmacking" == "fingerlicking"
```

### PHP example

```php
'lipsmacking' == 'fingerlicking'
```

## Determining the position at which one string occurs within another

All of the following examples evaluate to a 3, because the string
\'smack\' occurs at index position 3 within the string \'lipsmackingly
good\'.

### Python example

```python
'lipsmackingly good'.find('smack', 0)
```

### Java example

```java
"lipsmackingly good".indexOf("smack")
```

### Javascript example

```javascript
"lipsmackingly good".indexOf("smack")
```

### PHP example

```php
strpos('lipsmackingly good', 'smack')
```

## Determining whether one string occurs within another

All of the following examples evaluate to a boolean true value, because
the text \'smack\' occurs within the text \'lipsmackingly good\'.

### Python example

```python
'lipsmackingly good'.find('smack') >= 0
```

Note Python also has an \'in\' operator that can be used

```python
'smack' in 'lipsmackingly good'
```

### Java example

```java
"lipsmackingly good".indexOf("smack") >= 0
```

### Javascript example

```javascript
"lipsmackingly good".indexOf("smack") >= 0
```

### PHP example

```php
strpos('lipsmackingly good', 'smack') != false
```

## More string functions in Python

### String functions with Boolean return values

Image you have a few strings\...

```python
x = "Геркулес"
y = "лес"
z = "Герку"
```

Every string has built-in methods available to it that help analyze its
contents. These functions all return booleans:

- `x.endswith(y)`
- `x.startswith(y)`
- `x.islower()`
- `x.isupper()`
- `x.isalpha()`
- `x.isnumeric()`
- `x.isalnum()`
- `x.isdigit()`
- `x.isdecimal()`

### String functions that search and replace

- `x.find(y)`
- `x.rfind(y)`
- `x.replace(z, y)`
- `x.strip()`
- `x.count(y)`

### String functions that return a new copy of the string with case changes

- `x.capitalize()`
- `x.lower()`
- `x.upper()`
- `x.swapcase()`
- `x.title()`

### Formatting strings

- `x.format()` with named keywords
- `x.format()` with indices
- see [string formatting examples](./string-formatting)

### String functions that split strings into lists

- `x.split(y)`
- `x.rsplit(y)`
- [see more about Lists](list-basics)
