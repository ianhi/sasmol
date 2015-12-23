import sys

class log():

    def error(self, message):
        print '\n'+message+'\n'
        raise 

log = log()

try:

    filename = 'data.txt'

    file = open(filename).readlines()

except IOError as error:

    log.error("ERROR: I/O error({0}): {1}".format(error.errno, error.strerror) + " : " + filename)

except:

    log.error("ERROR: Unexpected error:" + str(sys.exc_info()[0]))


try:

    for line in file:

        value = int(line.strip())

except ValueError:
    
    log.error("ERROR: Could not convert data to an integer: \nline number in file = " + str(file.index(line) + 1) + "\nvalue = " + str(line))

except:

    log.error("ERROR: Unexpected error:" + str(sys.exc_info()[0]))
    
    
