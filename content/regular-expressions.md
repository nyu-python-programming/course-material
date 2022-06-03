---
layout: github
title: Regular Expressions
permalink: /regular-expressions
redirect_from: /regular-expressions.md
---

# Regular expressions

Raw strings are just another way to write string
[literals](Variables,_literals,_and_expressions#Variables_vs._Literals).

## Regular string literals

As [you surely know already](Variables_and_literals), Python
gives lots of ways to write string literals:

### Using single quotes

```python
 #with single quotes
 my_variable = 'my value"
```

### Using double quotes

```python
 #with double quotes
 my_variable = "my value"
```

### Using triple quotes

```python
#with triple single quotes
my_variable = '''my value'''
```

```python
#with triple double quotes
my_variable = """my value"""
```

## The problem: backslashes

In regular string literals, as you surely know already, backslashes have
special meaning. They indicate an escape character.

```python
 #a string with a line break in it, since \n in a string literal represents a line break
 waste_of_my_time = 'this\nexample'
```

```python
 #a string with a tab in it, since \t in a string literal represents a line break
 work_of_art = 'this\twebsite'
```

```python
 #a string with two double quotes in it, since \" is the escape character for a double quote
 genius_advice = "She said, \"Don't worry about it, it's ornithological!\""
```

```python
 #another string with an apostrophe (same character as single quote), since \' is an escaped single quote
 more_genius_advice = 'She said, "Don't worry about it, it\'s ornithological!"'
```

```python
 #a string with a single backslash in it, since \\ represents one backslash!
 getting_dizzy = 'C:\\Program Files'
```

```python
 #lots of escaped backslashes become difficult to read
 caput = 'C:\\Program Files\\^%(x86)\\Internet Explorer\\iexplore.exe'
```

and so on\...

## The solution: raw strings

In raw string literals, backslashes have no special meaning as an escape
character. This is useful for writing strings that contain a lot of
backslashes. Not having to escape each backslash makes the string more
readable.

```python
 #notice the r prefixe indicates a raw string literal
 less_caput = r'C:\Program Files\^%(x86)\Internet Explorer\iexplore.exe'
```

## Regular expressions are more easily written with raw string literals

[Regular expressions](Regular_expressions) usually contain a
lot of backslashes. When using Python\'s [re
module](https://docs.python.org/3.5/library/re.html), regular
expressions are represented as strings. So, like all strings with a lot
of backslashes, they are more readable when written in raw literal form.

```python
 #import Python's regular expressions module
 import regex

 #compile a regular expression... note the raw string literal that doesn't have its backslashes escaped
 p = re.compile(r'[Ee](\+|-)?[0-9]+')
```

In the above example, if we hadn\'t written regular expressions as a raw
string, we would have had to escape any backslashes, which would have
made the string even more difficult to read than it already is.

## Net net

[Net net](https://en.wiktionary.org/wiki/net_net), whichever way you do
it, your goal is to ultimately have a string representing the regular
expression as it is properly written in regular expressions syntax.
