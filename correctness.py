#!/usr/bin/env python

my_seed = 0
number_of_finds = 1.0   # fraction of total number of records
number_of_finds_by_name = 1   # fraction of total number of records
id_range_size = 1e9

import sys
import time
import CEP
import random
from numpy import average as avg

# Read data from file
lr = []     # list of records
ids_all = []
cs = {}
with open("test_data/data_10.txt", 'r') as f:
    l = f.readline()        # skip line
    n = int(f.readline())   # number of records
    for l in f:
        l = l.split()
        l[0] = int(l[0])
        ids_all.append(l[0])
        lr.append(l)
        cs[l[2]] = l[2]
print("\nDone reading data from file.")

print("\nTesting insertion.")
d = CEP.CEP_ADT()
for l in lr:
    d.insert(l[0], l[1], l[2], p=True)
#exit()

print("\n\nTesting find by ID\n")
# Find by ID
random.seed(my_seed)
keys = []
results = []
for m in range(int(n * number_of_finds)):
    i = random.randint(0, n - 1)
    keys.append(lr[i][0])
for k in keys:
    d.find(k, p=True)
#exit()

# List by range of id
print("\n\nTesting list by range of id:")
max_id = max(ids_all)
i2 = random.randint(0, max_id)
i1 = i2 - id_range_size
l = d.list_in_range(i1, i2, p=True)
#exit()

# List by city
print("\n\nTesting list by city:")
for c in cs:
    l = d.list_by_city(c, p=True)
#exit()

# Find by name
print("\n\nTesting list by name:")
keys = []
for m in range(int(n * number_of_finds_by_name)):
    keys.append(lr[random.randint(0, n - 1)][1])
for key in keys:
    l.append(d.find_by_name(key, p=True))

# Delete
for l in lr:
    d.delete(l[0], p=True)

