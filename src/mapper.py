#!/usr/bin/env python

"""
Mapper file to find average age of male and female dies in Titanic
"""

import sys

# Reading lines from the given dataset
# Remvoing trailing whitespaces using stip and
# splitting the lines.
for line in sys.stdin:
    line = line.strip()
    line = line.split(',')

    # By looking at the datset, we can know that
    # 4th and 5th columns are gender and age. Extracting
    # only them inorder to work. 
    print('%s,%s' % (line[4],line[5]))