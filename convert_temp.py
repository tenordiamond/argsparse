# this is a converter from cesius to fahrenheit and back
# Made mainly to learn how to parse strings from command line
import sys
import getopt
import argparse

#converts to fahrenheit
def fahr(x):
    x = (x - 32) / 1.8
    return x
#converts to celsius
def cel(x):
    x = (x * 1.8) + 32
    return x

# I create a ArgumentParser object
parser = argparse.ArgumentParser(description='Converts temperatures between Celsius and Fahrenheit.')

# Then I add my arguments and tell the parser how to take the
# strings from the command line and turn them into objects
parser.add_argument('integer', metavar='N', type=int, help='An integer to convert to either celsius or fahrenheit')
# I add arguments 
parser.add_argument('--toCels', dest='converted', action='store_const', const=cel, default=fahr, help='Converts an integer between celsius and fahrenheit (default: to fahrenheit)')


args = parser.parse_args()
print(args.converted(args.integer))