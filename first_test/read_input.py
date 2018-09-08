'''read_input.py: Read coordinates from a plain text file and transform them into a matrix.'''

import numpy as np
import math
from random import randint
import copy

line_start = 0
result = 0
pre_stripped = []
stripped_numbers = []
distances = []
distance_no_zero = []

# open file and extract data from it
with open('burma14-test.tsp') as f:
    x = [line.rstrip() for line in f]

# get the line where actual data starts
for element in x:
    pre_stripped.append(element.split())
    if "DISPLAY" and "NODE" in element:
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

for element in range(len(distances)):
    print(str(element).format("D2"), str(distances[element]))

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
first_search_index = search_index
search_history = []
# update_array[0] = remaining locations
# update_array[1] = current location
# update_array[2] = distance walked so far or result
update_list = [list(range(len(distance_no_zero))), [randint(0, len(distance_no_zero) - 1)], [result]]

print(update_list)



class Container:
    def __init__(self, distance_list, remaining_locations, current_location, first_location, distance):
        self.distance_list = distance_list
        self.distance_list_working = copy.deepcopy(self.distance_list)
        self.remaining_locations = remaining_locations
        self.current_location = current_location
        self.first_location = first_location
        self.distance = distance
        self.search_history = []

        self.remaining_locations.remove(self.first_location)
        for element in range(len(self.distance_list_working)):
            self.distance_list_working[element][self.first_location] = 999
        self.search_history.append(first_location)

    def __repr__(self):
        return "\nCONTAINER: " \
               "\ndistance_list:%s " \
               "\ndistance_list_working: %s" \
               "\nremaining_locations:%s" \
               "\ncurrent_location: %s" \
               "\nfirst_location: %s" \
               "\ndistance: %s" \
               "\nsearch_history: %s\n" % (self.distance_list, self.distance_list_working, self.remaining_locations, self.current_location,
                                   self.first_location, self.distance, self.search_history)


def update_step_container(container, next_location):

    if container.current_location in container.remaining_locations:
        container.remaining_locations.remove(container.current_location)
        container.search_history.append(container.current_location)

        for element in container.distance_list_working:
            element[container.current_location] = 999

    if container.remaining_locations:
        container.distance += container.distance_list[container.current_location][next_location]
    else:
        container.distance += container.distance_list[container.search_history[-1]][container.first_location]

    container.current_location = next_location

    return container


def naive_search():
    container = Container(distance_no_zero, list(range(len(distance_no_zero))), search_index, search_index, result)

    for element in range(len(container.distance_list)):

        next_min_distance = min(container.distance_list_working[container.current_location])
        next_location = container.distance_list_working[container.current_location].index(next_min_distance)

        container = update_step_container(container, next_location)

    # print dem bois
    print(container)
    print("CONTAINER METHOD")
    print(container.distance)
    print(container.search_history)

naive_search()


def update_step(update_list, distance_array, next_location):
    update_list[2] += distance_array[update_list([1])][next_location]
    update_list[0].remove(update_list([1]))
    update_list[1] = next_location

    if not update_list[0]:
        pass

    return update_list

# a naive min distance search
for element in range(len(distance_no_zero)):
    # print(search_index)
    search_history.append(search_index)

    min_distance = min(distance_no_zero[search_index])
    # print(min_distance)
    if min_distance is not 999:
        result += min_distance

    for kick_index in range(len(distance_no_zero)):
        distance_no_zero[kick_index][search_index] = 999

    search_index = distance_no_zero[search_index].index(min(distance_no_zero[search_index]))
    # print(distance_no_zero)
    # print(distance_no_zero[search_index].index(min(distance_no_zero[search_index])))

# add last part to close a circle
result += distances[first_search_index][search_history[-1]]

# print dem bois
print("OLD FOR METHOD")
print(result)
print(search_history)
