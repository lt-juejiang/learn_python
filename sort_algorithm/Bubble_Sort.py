#!/user/bin/python
#coding=utf-8

def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

def bubble_sort_flag(lists):
    count = len(lists)
    for i in range(0, count):
        flag = True
        for j in range(0, count-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
                flag = False
        if flag:
            return lists
    return lists

if __name__ == "__main__":
    lists = [12, 3, 5, 17, 48, 35, 6, 8]
    print('origin_lists:', lists)
    list1 = bubble_sort(lists)
    list2 = bubble_sort_flag(lists)
    print("bubble_sort:", list1)
    print("bubble_sort_flag:", list2)
