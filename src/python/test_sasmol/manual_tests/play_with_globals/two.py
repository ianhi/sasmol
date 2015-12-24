import sys

sys.path.append('./')

import sasmol as sasmol

class two_class():
    def __init__(self):
        self._id = sasmol.__sasmol_id__ + 1
        sasmol.__sasmol_id__ += 1

    def __del__(self):
        sasmol.__sasmol_id__ -= 1
        del self
    
print ; print 'IN TWO' ; print

sasmol.__sasmol_debug__ = True
sasmol.__sasmol_logging__ = True

print 'creating instance a'
a = two_class()
#with two_class() as a
print 'in two: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__

print 'creating instance b'
b = two_class()
print 'in two: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__

#a.__del__
#b.__del__

del a,b


'''
print 'in two: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__
print 'in two: sasmol.__sasmol_debug__ = ',sasmol. __sasmol_debug__
print 'in two: sasmol.__sasmol_logging__ = ', sasmol.__sasmol_logging__

print ; print 'incrementing variables'

sasmol.__sasmol_id__ += 1
sasmol.__sasmol_debug__ = True
sasmol.__sasmol_logging__ = True

print 'in two: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__
print 'in two: sasmol.__sasmol_debug__ = ',sasmol. __sasmol_debug__
print 'in two: sasmol.__sasmol_logging__ = ', sasmol.__sasmol_logging__

print

'''


