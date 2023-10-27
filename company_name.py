#!/bin/python3

def sortfuncalpha(element):
    return element[1]
def sortfuncnum(element):
    return element[0]

if __name__ == '__main__':
    s = input()
    count = {}
    list_ = []

    for i in s:  # to count each element
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            list_.append(i)  # this is to keep track of each individual letter in the name

    new_l = []
    for i in list_:  # this is to create a new 2d list with elements their counts, so that we can sort it later
        
        new_l.append([count[i], i])

    new_l.sort(key=sortfuncalpha)  # first we sort alphabetically

    new_l.sort(key=sortfuncnum,reverse=True) # then we sort by the most repeating elements
        
    to_print = new_l[:3]  # this gets the top 3 most repeated letters in order
    for i in to_print:
        print(i[1], i[0])
