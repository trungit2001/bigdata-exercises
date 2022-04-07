#!/usr/bin/env python
import sys

current_country = None
current_city = None
count = 1

for line in sys.stdin:
    line = line.strip()
    country, city = line.split('\t', 1)

    if current_country == country and current_city != city:
        count += 1
        current_city = city
    elif current_country == country and current_city == city:
        continue
    else:
        if current_country:
            print('%s\t%s' % (current_country, count))
            count = 1
        current_country = country
        current_city = city

if current_country == country:
    print('%s\t%s' % (current_country, count))