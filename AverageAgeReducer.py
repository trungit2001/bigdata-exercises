#!/usr/bin/env python
import sys

current_gender = None
min_age = 0
max_age = 0

for line in sys.stdin:
	line = line.strip()
	gender, age = line.split(',', 1)

	try:
		age = float(age)
	except ValueError:
		continue

	if current_gender == gender:
		if min_age > age:
			min_age = age
		if max_age < age:
			max_age = age
	else:
		if current_gender:
			print(f'{current_gender}\t{min_age}\t{max_age}')
		current_gender = gender
		min_age = age
		max_age = min_age

if current_gender == gender:
	print(f'{current_gender}\t{min_age}\t{max_age}')
