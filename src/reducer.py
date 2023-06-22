#!/usr/bin/env python

"""
Reducer file to find average age of male and female dies in Titanic
"""

import sys

male_sum = 0
female_sum = 0
count_fem = 0
count_male = 0

for line in sys.stdin:
    line = line.strip()
    gender, age = line.split(',')

    # Adding initial condition to only access the records with
    # valid age in order to avoid any calcuation error
    if (age != ''):
        # Conditions to calcualte based on gender
        if gender == 'female':
            count_fem += 1
            female_sum += float(age)
        
        elif gender == 'male':
            count_male += 1
            male_sum += float(age)
    else:
        # Incase the record does not contain valid age
        # quitely move forward
        continue

print("Average female age = %s" % (female_sum/count_fem))
print("Average male age = %s" % (male_sum/count_male))