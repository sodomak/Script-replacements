#!/usr/bin/python2

import sys
import argparse

parser = argparse.ArgumentParser(description='Slower alternative to strings.')
parser.add_argument('file', metavar='FILENAME', type=str, nargs=1, 
                    help='File to parse')
parser.add_argument('--radix', '-t', type=str,
                    choices=['o','d','x'],
                    help='Print the location of the string in base 8, 10 or 16')
parser.add_argument('--strlen', '-N', metavar='<number>', type=int, nargs='?', default=4,
                    help='least [number] characters (default 4).')

args = parser.parse_args()

def printOffset(lnr):
    return {
            'o': oct(lnr) + ' ',
            'd': str(lnr) + ' ',
            'x': hex(lnr) + ' '
            }.get(args.radix, '')


filename = str(sys.argv[1])
output = ""
line = ""
cont = False
offset = 0
linenr = 0

with open(filename) as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if (ord(c) >= 32) and (ord(c) <= 126) :
            line = line + c
            if cont == False:
                offset = linenr
            cont = True
        else:
            if (cont == True):
                if len(line) >= args.strlen:
                    line = printOffset(offset) + line
                    output = output + line + "\n"
                    cont = False
                    line = ""
                else:
                    line = ""
                    cont = False
            else:
                line = ""
                cont = False
        linenr = linenr + 1

print output
