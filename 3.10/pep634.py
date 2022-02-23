# Structural Pattern Matching: Specification
import sys

match int(sys.argv[1]):
    case 1:
        print (1)
    case 2:
        print (2)
    case _: # default pattern
        print (f'default: {sys.argv[1]}')
