#!/usr/bin/env python3
# -*- coding:utf8 -*-

st1 = ' wo shi, Cheng Long da ge ! '
st2 = '12'


print(st1.capitalize())
print(st1.center(40))
print(st1.count('da'))
by = st1.encode(encoding='utf-8', errors='strict')
print(type(by))
st3 = by.decode(encoding='utf-8', errors='strict')
print(type(st3))
print(st1.endswith('!'))
print(st1.expandtabs(tabsize=1))
print(st1.find('s'))
print(st1.index('s'))
print(st1.format())
print(st1.isalnum())
print(st1.isalpha())
print(st1.isdecimal())
print(st1.isdigit())
print(st1.islower())
print(st1.isnumeric())
print(st1.isspace())
print(st1.istitle())
print(st1.isupper())
print(st1.join(st2))
print(st1.ljust(40))
print(st1.lower())
print(st1.lstrip())
print(st1.maketrans('wo', 'Wo'))
print(max(st1), min(st1))
print(st1.partition('Cheng'))
print(st1.replace('wo', 'Wo'))
print(st1.rstrip())
print(st1.split(','))
print(st1.splitlines())
print(st1.startswith(' '))
