#!/user/bin/python
#coding=utf-8

def quick_sort(list, left, right):
    key = list[left]
    low = left
    high = right
    while low < high:

        while low < high and list[high] >= key:
            high -= 1
        list[left] = list[high]
        while low < high and list[low] <= key:
            low += 1
        list[high] = list[low]
    list[low]= key
    quick_sort(list, left, high-1)
    quick_sort(list, low+1, right)
    return list