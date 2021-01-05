import re

# match() : checks for a match that is at the BEGINNING of the string. returns bool.
# search(): checks for a match ANYWHERE in the string. returns bool.

text = "This is a good day"

if re.search("good", text):
    print('Wonderful!')
else:
    print('Alas:(')

if re.match("good", text):
    print('Wonderful!')
else:
    print('Alas:(')


# split() : tokenize using delimiter. returns list
# findall() : finds all occurrences of given token. returns list
text = 'Amy works diligently. Amy gets good grades. Our student Amy is successful.'

print('split():', re.split('Amy', text))
print('findall():', re.findall("Amy", text))

# ^(caret) : ^[string] to find word beginning with string. return Match object.
# $        : [string]$ to find word ending with string
print('^ :', re.search("^Amy", text))

# [](set operator) : [Patterns] to find patterns as if they were separated by OR
grades = 'ACAAAABCBCBAA'
print('[] :', re.findall("[AB]", grades))

# - : [Pattern start - Pattern end] to set range between start and end.
print('- :', re.findall("[A][B-C]", grades))

# | : OR
print('| :', re.findall("AB|AC", grades))

# [^] : caret inside [] is used to negate the results
print('[^]: ', re.findall('[^A]', grades))


### QUANTIFIERS

# {} : min, max consecutive.
print('{} :', re.findall('A{2,10}', grades))

# *(asterix) : match 0+
# ?          : match 1+
with open('datasets/ferpa.txt', 'r') as f:
    wiki = f.read()

print(wiki)

print('Get headers')
# NOTE: [] surrounding 'edit' is escaped because they are part of the pattern to search for
print(re.findall("[a-zA-Z]{1,100}\[edit\]", wiki))
# \w : meta character for any letters [a-zA-Z]
# \s : white space
print(re.findall("[\w]{1,100}\[edit\]", wiki))
# *(asterix) : match 0+
print(re.findall("[\w ]*\[edit\]", wiki))

print('titles:')
for title in re.findall("[\w ]*\[edit\]", wiki):
    print(re.split("[\[]", title)[0])

### GROUPS

# () : use parentheses to group patterns together
print('() :', re.findall("([\w ]*)(\[edit\])",wiki))

# if we want the results in Match Objects, use finditer() : returns tuples
for item in re.finditer("([\w ]*)(\[edit\])",wiki):
    print(item.groups())

# ?P<name> : to give group name. Then use groupdict()
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
    print(item.groupdict()['title'])

# ?= : look ahead to isolate
print('?=')
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])",wiki):
    print(item)

# re.VERBOSE : allows multi-line regex
with open('datasets/buddhist.txt', 'r') as f:
    wiki = f.read()
print(wiki)
pattern="""
(?P<title>.+)
(\ –\ located\ in\ ) # NOTE - is not ordinary dash
(?P<city>\w*)
(,\ )
(?P<state>\w*)
"""
print('pattern:', pattern)

for item in re.finditer(pattern,wiki,re.X):
    print('here')
    print(item.groupdict())
print('done')
