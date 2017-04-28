#! python3
# password.py - Checks string for strength.

import re, sys

def passwordCheck(password):
    lowerCheck = re.compile('[a-z]+')
    upperCheck = re.compile('[A-Z]+')
    digitCheck = re.compile('\d+')

    if len(password) < 7:
        print('Password should have 8 characters or greater')
        sys.exit()
    
    lowerPass = lowerCheck.search(password)
    if lowerPass == None:
        print('Need at least one lowercase character')
        sys.exit()
    
    upperPass = upperCheck.search(password)
    if upperPass == None:
        print('Need at least one uppercase character')
        sys.exit()
    
    digitPass = digitCheck.search(password)
    if digitPass == None:
        print('Need at least one digit')
        sys.exit()

    print('Password is good')




print('Input password')
password = input()
passwordCheck(password)




