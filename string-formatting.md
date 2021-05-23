# Formatting strings

Examples of formatting [strings in Python](Strings "wikilink") using the
built-in [string format()
function](https://docs.python.org/3/library/string.html#format-examples).

- The expected output of each example is displayed as a comment.
- Note that the format [function](Functions "wikilink") always returns
  a string.

## The basic idea

Unlabeled placeholders:

`x = '{}, {}, {}'.format('a', 'b', 'c')`\
`print(x)`\
`#'a, b, c'`

Numerical indices as placeholders

`x = '{0}, {1}, {2}'.format('a', 'b', 'c')`\
`print(x)`\
`#'a, b, c'`

Named placeholders:

`x = '{first}, {second}, {third}'.format(first='a', second='b', third='c')`\
`print(x)`\
`#'a, b, c'`

## Mixing it up

Numerical indices out of order:

`x = '{2}, {1}, {0}'.format('a', 'b', 'c')`\
`print(x)`\
`#'c, b, a'`

Repeating placeholders more than once:

`x = '{0}{1}{0}'.format('abra', 'cad')`\
`print(x)`\
`#'abracadabra'`

## Alignment

Left-aligned within 20 spaces:

`x = format('Harry', '<20s')`\
`print(x)`\
`#'Harry '`

Right-aligned within 20 spaces:

`x = format('Barry', '>20s')`\
`print(x)`\
`#' Barry'`

Center-aligned within 20 spaces:

`x = format('Harry', '^20s')`\
`print(x)`\
`#' Harry '`

Right-aligned within 20 spaces with the \'\*\' as a fill character:

`x = format('Harry', '*>20s')`\
`print(x)`\
`#'***************Harry'`

Center-aligned within 20 spaces with the \'-\' as a fill character:

`x = format('Barry', '-^20s')`\
`print(x)`\
`#'-------Barry--------'`

## Combining formatted strings

A string left-aligned within 20 spaces, combined with another string
left-aligned within 10 spaces:

`x = format('Harry', '<20s')`\
`y = format('$20', '<10s')`\
`z = "{0}{1}".format(x, y) #`[` remember`` ``this `](#The_basic_idea "wikilink")`?!`\
`print(z)`\
`#'Harry $20 '`

## Limiting decimal places

Two decimal places:

`x = format(0.33333333, '.2f')`\
`print(x)`\
`#'0.33'`

Five decimal places:

`x = format(0.33333333, '.5f')`\
`print(x)`\
`#'0.33333'`

Commas for thousands:

`x = format(33333333.22222222, ',.5f')`\
`print(x)`\
`#'33,333,333.22222'`

Right-aligned:

`x = format (33333333.22222222, '>20,.2f')`\
`print(x)`\
`# ' 33,333,333.22'`

Percentage conversion:

`x = format(0.52, '%')`\
`print(x)`\
`#'52.000000%'`

Percentage conversion with limited decimal places:

`x = format(0.52, '.2%')`\
`print(x)`\
`#'52.00%'`

Percentage conversion with no decimal places:

`x = format(0.52, '.0%')`\
`print(x)`\
`#'52%'`

Left-aligned with percentage conversion and limited decimal places:

`x = format(0.52, '<20.2%')`\
`print(x)`\
`#'52.00% '`

## Integer numbers with commas

An integer, with commas for thousands:

`x = format(5200, ',d')`\
`print(x)`\
`#'5,200'`

An integer, with commas for thousands, left-aligned within 20 spaces:

`x = format(5200, '<20,d')`\
`print(x)`\
`#'5,200 '`

An integer, with commas for thousands, right-aligned within 20 spaces:

`x = format(5200, '>20,d')`\
`print(x)`\
`#' 5,200'`
