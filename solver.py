#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from knapsack import format_data
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    results = format_data(input_data)
    # lines = input_data.split('\n')

    # firstLine = lines[0].split()
    # item_count = int(firstLine[0])
    # capacity = int(firstLine[1])


    # items = []

    # for i in range(1, item_count+1):
    #     line = lines[i]
    #     parts = line.split()
    #     items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # # a trivial greedy algorithm for filling the knapsack
    # # it takes items in-order until the knapsack is full
    # value = 0
    # weight = 0
    # taken = [0]*len(items)

    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight
    
    # # prepare the solution in the specified output format
    # output_data = str(value) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, taken))
    # print output_data
    return results


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

