#!/usr/bin/env python
import sys

current_device_id = None
sum_x = 0
device_id = None

for line in sys.stdin:
    line = line.strip()
    device_id, x = line.split('\t', 1)

    try:
        x = float(x)
    except ValueError:
        continue

    if current_device_id == device_id:
        sum_x += x
    else:
        if current_device_id:
            print('%s\t%s' % (current_device_id, round(sum_x, 1)))
        sum_x = x
        current_device_id = device_id

if current_device_id == device_id:
    print('%s\t%s' % (current_device_id, round(sum_x, 1)))
