#!/usr/bin/env python3
# 2022-05-05 A simple python password generator  

import random, string

lenght = int(input('password lenght: '))
print('Choose options:')
choice = input(('(n)umbers, (l)etters, (s)ymbol: '))
choice = choice.lower()

options = ['nsl', 'nls', 'snl', 'sln', 'lsn', 'lns']

for i in range(lenght):

    if choice == 'n':
        num = string.digits
        numpsw = "".join(random.sample(num, 1))
        print(numpsw, end="")
    if choice == 'l':    
        letters = string.ascii_letters
        letpsw = random.choice(letters)
        print(letpsw, end="")
    if choice == 's':    
        pon = string.punctuation
        popsw = random.choice(pon) 
        print(popsw, end="")

    if choice == 'ns' or choice == 'sn':
        ns = string.digits + string.punctuation
        nspsw = "".join(random.sample(ns, 1))
        print(nspsw, end="")

    if choice == 'nl' or choice == 'ln':
        nl = string.digits + string.ascii_letters
        nlpws = "".join(random.sample(nl, 1)) 
        print(nlpws, end="")

    if choice == 'ls' or choice == 'sl':
        ls = string.ascii_letters + string.punctuation
        lspsw = "".join(random.sample(ls, 1))
        print(lspsw, end="")
    
    if len(choice) == 3 and choice in options: 
        nls = string.digits + string.ascii_letters + string.punctuation
        nlspsw = "".join(random.sample(nls, 1))
        print(nlspsw, end="")
    
print("")
exit