'''read_input.py: Read coordinates from a plain text file and transform them into a matrix.'''

import numpy as np
import math
from random import randint

line_start = 0
result = 0
pre_stripped = []
stripped_numbers = []
distances = []
distance_no_zero = []

# open file and extract data from it
with open('burma14.tsp') as f:
    x = [line.rstrip() for line in f]

# get the line where actual data starts
for element in x:
    pre_stripped.append(element.split())
    if "SECTION" and "NODE" in element:
        line_start = x.index(element) + 1
        # print(x.index(element))


# strip empty elements and afterwards strip EOF in the end of the list
pre_stripped = list(filter(None, pre_stripped))
pre_stripped = pre_stripped[line_start:-1]
pre_stripped = np.array(pre_stripped)

# get distances from list, calculated by simple coordinates
for element in pre_stripped.astype(np.float):
    dist_part = []
    for element_n_two in pre_stripped.astype(np.float):
        dist = math.hypot(element_n_two[1] - element[1], element_n_two[2] - element[2])
        dist_part.append(round(dist, 1))
    distances.append(dist_part)

# prepare distances list so no 0 element occurs anymore
# switch 0 for 9999999, so min can be calculated properly
for element in distances:
    dist_corr = []
    for element_n_two in element:
        if element_n_two == 0:
            element_n_two = 999
        dist_corr.append(element_n_two)
    distance_no_zero.append(dist_corr)


# set search index and history
search_index = randint(0, len(distance_no_zero) - 1)
search_history = []

# a naive min distance search
for element in range(len(distance_no_zero)):
    print(search_index)
    search_history.append(search_index)

    min_distance = min(distance_no_zero[search_index])

    if min_distance is not 999:
        result += min_distance

    for kick_index in range(len(distance_no_zero)):
        distance_no_zero[kick_index][search_index] = 999

    search_index = distance_no_zero[search_index].index(min(distance_no_zero[search_index]))
    print(distance_no_zero)
    # print(distance_no_zero[search_index].index(min(distance_no_zero[search_index])))

# print dem bois
print(result)
print(search_history)
