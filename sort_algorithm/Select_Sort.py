#!/user/bin/python
#coding=utf-8

def select_sort(list):
    count = len(list)
    for i in range(0,count):
        min = i
        for j in range(i+1,count):
            if list[j] < list[min]:
                min = j
        list[min], list[i] = list[i], list[min]
    return list

if __name__ =="__main__":
    list = [12, 3, 5, 17, 48, 35, 6, 8]
    print('origin_list:', list)
    list1 = select_sort(list)

    print("select_sort:", list)
