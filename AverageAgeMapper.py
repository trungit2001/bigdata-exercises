#!/usr/bin/env python
import sys
cnt = 1
for line in sys.stdin:
    line = line.strip()
    

    try:
        line = line.split(',')
        gender = line[4]
        age = line[5]

        if age != '':
            print(f'{gender},{age}')
    except:
        continue