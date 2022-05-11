#!/usr/bin/env python3

import random, string, argparse, sys

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Python Password Generator')

parser.add_argument('-n', '--number', action="store_true", help='Generate only Numbers')
parser.add_argument('-a', '--alpha', action="store_true", help='Generate only alphabetical characters')
parser.add_argument('-s', '--symbol', action="store_true", help='Generate only symbols')
parser.add_argument('length', type=int, help='The length of the Password')

args = parser.parse_args()

length = args.length
options = ['-nsa', '-nas', '-sna', '-san', '-asn', '-ans']

for i in range(length):

    if '-n' in sys.argv or '--number'in sys.argv:
        num = string.digits
        numpsw = "".join(random.sample(num, 1))
        print(numpsw, end="")

    if '-a' in sys.argv or '--alpha' in sys.argv:
        letters = string.ascii_letters
        letpsw = random.choice(letters)
        print(letpsw, end="")

    if '-s' in sys.argv or '--symbol' in sys.argv:    
        pon = string.punctuation
        popsw = random.choice(pon) 
        print(popsw, end="")

    if '-ns' in sys.argv or '-sn' in sys.argv:
        ns = string.digits + string.punctuation
        nspsw = "".join(random.sample(ns, 1))
        print(nspsw, end="")

    if '-na' in sys.argv or '-an' in sys.argv:
        nl = string.digits + string.ascii_letters
        nlpws = "".join(random.sample(nl, 1)) 
        print(nlpws, end="")

    if '-as' in sys.argv or '-sa' in sys.argv:
        ls = string.ascii_letters + string.punctuation
        lspsw = "".join(random.sample(ls, 1))
        print(lspsw, end="")
    
    if len(sys.argv[2]) == 4:
        nls = string.digits + string.ascii_letters + string.punctuation
        nlspsw = "".join(random.sample(nls, 1))
        print(nlspsw, end="")
    
print("")
exit

