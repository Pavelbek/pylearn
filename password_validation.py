__author__ = 'Paul'

import re


fl1 = 'A1213pokl'
tr1 = 'bAse730onE4'
fl2 = 'asasasasasasasaas'
fl3 = 'QWERTYqwerty'
fl4 = '123456123456'
tr2 = 'QwErTy911poqqqq'


def checkio(data):
    if len(data) >= 10:
        result = [re.search(r'[0-9]', data), re.search(r'[a-z]', data), re.search(r'[A-Z]', data)]
        if None not in result:
            return True
    return False

print(checkio(fl1))

# not mine solution

import re
def checkio(data):
    if re.match('^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z]).{10,}$', data):
        return True 
    else:
        return False
		
