#!/usr/bin/env python
import sys

current_embarked_code = None
current_count = 0
embarked_code = None

for line in sys.stdin:
	line = line.strip()
	embarked_code, count = line.split('\t', 1)
	try:
		count = int(count)
	except ValueError:
		continue

	if current_embarked_code == embarked_code:
		current_count += count
	else:
		if current_embarked_code:
			print('%s\t%s' % (current_embarked_code, current_count))
		current_count = count
		current_embarked_code = embarked_code

if current_embarked_code == embarked_code:
	print('%s\t%s' % (current_embarked_code, current_count))
