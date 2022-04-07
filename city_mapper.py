#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(',')
    city = line[5]
    country = line[7]

    if not country == 'Country' and city != 'City':
        print(f'{country.strip()}\t{city.strip()}')
