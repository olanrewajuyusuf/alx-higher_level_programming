#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list:
        if i == idx and idx >= 0:
            return idx
