#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    device_id, x = line.split(',')

    print('%s\t%s' % (device_id, 1))
