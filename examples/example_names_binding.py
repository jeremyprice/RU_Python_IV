#!/usr/bin/env python3


def list_widget(in_list):
    in_list[0] = 10

    in_list = list(range(1, 10))
    print(in_list)
    in_list[0] = 10
    print(in_list)


my_list = [9, 9, 9, 9]
list_widget(my_list)
print(my_list)
