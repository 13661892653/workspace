#coding="utf-8"
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

string=input("input str:")
lst=string.split(',')
sortAfter=bubble_sort(lst)
print('排序后',sortAfter)