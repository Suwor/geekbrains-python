from itertools import count, cycle


def count_generator(start, end):
    for item in count(start):
        if item >= end:
            break
        else:
            yield item


def cycle_generator(cycle_list, end):
    counter = 0
    for item in cycle(cycle_list):
        if counter >= end:
            break
        else:
            counter += 1
            yield item


for el in count_generator(10, 20):
    print(el)

for el in cycle_generator('ABC', 10):
    print(el)
