formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    '\n I had this thing.\n',
    'That you could type up right.\n',
    "But it didn't sing.\n",
    'So I said goodnight.'
))

# add a line break at the end of each line of the previous poem

