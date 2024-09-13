"""(Correct 7/7) Sol #1: 0.05s"""

newAlph = {
    'a' : '@',
    'b' : '8',
    'c' : '(',
    'd' : '|)',
    'e' : '3',
    'f' : '#',
    'g' : '6',
    'h' : '[-]',
    'i' : '|',
    'j' : '_|',
    'k' : '|<',
    'l' : '1',
    'm' : '[]\/[]',
    'n' : '[]\[]',
    'o' : '0',
    'p' : '|D',
    'q' : '(,)',
    'r' : '|Z',
    's' : '$',
    't' : "']['",
    'u' : '|_|',
    'v' : '\/',
    'w' : '\/\/',
    'x' : '}{',
    'y' : '`/',
    'z' : '2',
}

import sys

for line in sys.stdin:
    translation = ""
    for character in line:
        if character.lower() in newAlph:
            translation += newAlph[character.lower()] 
        else: translation += character
    print(translation)