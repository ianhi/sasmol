import sys
import weakref

sys.path.append('./')

import sasmol as sasmol

print 'in test: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__
print 'in test: sasmol.__sasmol_debug__ = ',sasmol. __sasmol_debug__
print 'in test: sasmol.__sasmol_logging__ = ', sasmol.__sasmol_logging__
print 

for i in xrange(10):
    sasmol.__sasmol_id__ += 1

print 'in test: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__
print 

print
print 'calling two'
print

import two as two

print
print 'back in test' ; print

print 'in test: sasmol.__sasmol_id__ = ', sasmol.__sasmol_id__
print 'in test: sasmol.__sasmol_debug__ = ',sasmol. __sasmol_debug__
print 'in test: sasmol.__sasmol_logging__ = ', sasmol.__sasmol_logging__

print

