spam = 'Hello world!'

print(spam[1:3])

spam.upper()

print("""
isalpha()	returns True if the string consists only of letters.
isalnum()	returns True if the string consists only of letters and numbers.
isdecimal()	returns True if the string consists only of numbers.
isspace()	returns True if the string consists only of spaces, tabs, and new-lines.
istitle()	returns True if the string consists only of words that begin with
                            an uppercase letter followed by only lowercase characters.
""")

'Hello world!'.startswith('Hello')
# True

'Hello world!'.endswith('world!')
# True

'abc123'.startswith('abcdef')
# False

'abc123'.endswith('12')
# False

'Hello world!'.startswith('Hello world!')
# True

'Hello world!'.endswith('Hello world!')
# True

print(' '.join(['My', 'name', 'is', 'Simon']))
'My name is Simon'

'My name is Simon'.split()
# ['My', 'name', 'is', 'Simon']

'MyABCnameABCisABCSimon'.split('ABC')
# ['My', 'name', 'is', 'Simon']

'My name is Simon'.split('m')
# ['My na', 'e is Si', 'on']

' My  name is  Simon'.split()
# ['My', 'name', 'is', 'Simon']

' My  name is  Simon'.split(' ')
# ['', 'My', '', 'name', 'is', '', 'Simon']

spam = '    Hello World     '
spam.strip()
# 'Hello World'

spam.lstrip()
# 'Hello World     '

spam.rstrip()
# '    Hello World'

spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')
# 'BaconSpamEggs'


a = 10000000
f"{a:,}"
# '10,000,000'
a = 3.1415926
f"{a:.2f}"
# '3.14'