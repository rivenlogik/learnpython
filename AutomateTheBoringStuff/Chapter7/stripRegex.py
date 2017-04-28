#! python3
#stripRegex.py - Strip whitespace or special char from front/back of string passed to function

import re,sys

def stripTool(string,substring=' '):
    stripBoth = re.compile('^{0}+|{0}+$'.format(substring))
    newString = stripBoth.sub('',string)
    print(newString)

print('Input a string')
stringIn = input()
print('Input a string to search for if not whitespace:')
subIn = input()
stripTool(stringIn,subIn)
stripTool(stringIn)


    
