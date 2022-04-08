#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    
    try:
        embarked_code = line[11]
        if embarked_code != '':
            print(f'{embarked_code}\t1')
    except:
        continue
