#!/usr/bin/env python
import sys

current_device_id = None
min_x = None
max_x = None
device_id = None

for line in sys.stdin:
    line = line.strip()
    device_id, x = line.split('\t', 1)

    try:
        x = float(x)
    except ValueError:
        continue

    if current_device_id == device_id:
        max_x = x if x > max_x else max_x
        min_x = x if x < min_x else min_x

    else:
        if current_device_id:
            print(f'{current_device_id}\t{min_x}\t{max_x}')
        min_x = x
        max_x = min_x
        current_device_id = device_id

if current_device_id == device_id:
    print(f'{current_device_id}\t{min_x}\t{max_x}')
