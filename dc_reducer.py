#!/usr/bin/env python
import sys

current_device_id = None
current_count = 0
device_id = None

for line in sys.stdin:
    line = line.strip()
    device_id, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_device_id == device_id:
        current_count += count
    else:
        if current_device_id:
            print('%s\t%s' % (current_device_id, current_count))
        current_count = count
        current_device_id = device_id

if current_device_id == device_id:
    print('%s\t%s' % (current_device_id, current_count))
