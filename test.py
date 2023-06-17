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
#with open("test_data/data_10.txt", 'r') as f:
#with open("test_data/data_100000.txt", 'r') as f:
with open("test_data/data_1000000.txt", 'r') as f:
    l = f.readline()        # skip line
    n = int(f.readline())   # number of records
    for l in f:
        l = l.split()
        l[0] = int(l[0])
        ids_all.append(l[0])
        lr.append(l)
        cs[l[2]] = l[2]
print("Done reading data from file.")
#time.sleep(2)
#exit()

# Insertion
ts1 = []
for k in range(5):
    t = time.time()
    d = CEP.CEP_ADT()
    #print(d)
    for l in lr:
        d.insert(l[0], l[1], l[2])
    ti = time.time() - t
    print(f'Insertion: \t\t {ti:.2f} s')
    ts1.append(ti)
ti = avg(ts1)
print(f'Insertion average: \t\t\t {ti:.2f} s')

#print(d)

# Find by ID
ts2 = []
random.seed(my_seed)
for k in range(5):
    keys = []
    for m in range(int(n * number_of_finds)):
        keys.append(lr[random.randint(0, n - 1)][0])
    #print(keys)
    #print(d.find(keys[0]))
    l = []
    t = time.time()
    for key in keys:
        l.append(d.find(key))
    tf = time.time() - t
    print(f'Find by ID: \t\t {tf:.2f} s')
    ts2.append(tf)
tf = avg(ts2)
print(f'Find by ID average: \t\t\t {tf:.2f} s')

#print(l)

# List by range of id
max_id = max(ids_all)
ts3 = []
for k in range(5):
    i2 = random.randint(0, max_id)
    i1 = i2 - id_range_size
    t = time.time()
    l = d.list_in_range(i1, i2)
    tl = time.time() - t
    print(f'List by ID range: \t {tl:.2f} s')
    ts3.append(tl)
tl = avg(ts3)
print(f'List by ID range average: \t\t {tl:.2f} s')

#print(l)

# List by city
ts4 = []
for c in cs:
    t = time.time()
    l = d.list_by_city(c)
    tlc = time.time() - t
    print(f'List by city: \t\t {tlc:.2f} s')
    ts4.append(tlc)
tlc = avg(ts4)
print(f'List by city average: \t\t\t {tlc:.2f} s')

# Find by name
ts5 = []
for k in range(5):
    keys = []
    for m in range(int(n * number_of_finds_by_name)):
        keys.append(lr[random.randint(0, n - 1)][1])
    #print(keys)
    #print(d.find_by_name(keys[0]))
    l = []
    t = time.time()
    for key in keys:
        l.append(d.find_by_name(key))
    tfn = time.time() - t
    print(f'Find by name: \t\t {tfn:.2f} s')
    ts5.append(tfn)
tfn = avg(ts5)
print(f'Find by name average: \t\t\t {tfn:.2f} s')

# Delete
t = time.time()
for l in lr:
    d.delete(l[0])
td = time.time() - t
print(f'Delete: \t\t\t\t {td:.2f} s')
print(f'Empty CEP_ADT: {d}')

#print(sys.getsizeof(d))
#print(sys.getsizeof(lr))
