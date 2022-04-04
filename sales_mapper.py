#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    country = line.split(',')[7]

    if not country == 'Country':
        print('%s\t%s' % (country, 1))
