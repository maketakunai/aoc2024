#!/usr/bin/env python3

with open('./input/01.txt') as input_file:
    #Begin part 1
    left_list, right_list = [],[]
    for i in input_file.read().splitlines():
        a,b = i.split()
        left_list.append(int(a))
        right_list.append(int(b))
    sum = 0
    for a,b in zip(sorted(left_list), sorted(right_list)):
        sum += abs(a-b)
    print('Part 1:',sum)

    #Begin part 2
    sim_score = 0
    for j in left_list:
        sim_score += (j * right_list.count(j))
    print('Part 2:',sim_score)