import sasmol.sasmol as sasmol
#### THIS is to see if we can use our own instance of Error(Exception) ...
#### not sure this will work cleanly or no
#### recommended by Google

Error = sasmol.Error()

#try: 
#    raise Error
#except Error as error: 
#    raise Error('why are you dividing my zero?')

#finally:
#    print 'wtf'

