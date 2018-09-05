'''read_input.py: Read coordinates from a plain text file and transform them into a matrix.'''

import numpy as np
import math

line_start = 0
result = 0
pre_stripped = []
stripped_numbers = []
distances = []
distance_no_zero = []

# open file and extract data from it
with open('burma14.tsp') as f:
    x = [line.rstrip() for line in f]

# print(x)

# get the line where actual data starts
for element in x:
    pre_stripped.append(element.split())
    if "SECTION" and "NODE" in element:
        line_start = x.index(element) + 1
        print(x.index(element))


# strip empty elements and afterwards strip EOF in the end of the list
pre_stripped = list(filter(None, pre_stripped))
pre_stripped = pre_stripped[line_start:-1]

pre_stripped = np.array(pre_stripped)
stripped_numbers = pre_stripped.astype(np.float)

# get distances from list, calculated by simple coordinates
for element in stripped_numbers:
    dist_part = []
    for element_n_two in stripped_numbers:
        dist = math.hypot(element_n_two[1] - element[1], element_n_two[2] - element[2])
        dist_part.append(round(dist, 1))
    distances.append(dist_part)

# print(distances)

# prepare distances list so no 0 element occurs anymore

print(distances)

# switch 0 for 9999999, so min can be calculated properly
for element in distances:
    dist_corr = []
    for element_n_two in element:
        if element_n_two == 0:
            element_n_two = 999999999
        dist_corr.append(element_n_two)
    distance_no_zero.append(dist_corr)

for element in distance_no_zero:
    print(min(element))

print(distance_no_zero)

# start to implement naive hillclimbing shizzle
for element in range(len(distances)):
    result += min(distances[element])
    distances.index(min(distances[0]))
    # update()


def hillclimbing(distances, result):
    pass
    # for

    # return "array", "updated result"



