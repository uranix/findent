#!/bin/bash python

import sys

def graph(v):
    return v in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

def iscont(line):
    return line[:5] == ' '*5 and graph(line[5])

def main():
    prev = ''

    for line in sys.stdin:
        while line and line[-1] in '\r\n':
            line = line[:-1]

        if not line:
            print line
            continue

        if line[0].upper() == 'C':
            print line
            continue

        if line.strip()[0] == '!':
            print line
            continue

        if iscont(line):
            prev += line[6:]
        else:
            if prev:
                print prev
            prev = line
    if prev:
        print prev

if __name__=='__main__':
    main()
