#coding=utf-8
#功能：(BubbleSort)冒泡排序算法
#作者：陈伦
#日期：2016-01-16
list=[100,10099,88,77,66,55,11,1,0,100,1]

def SortBy(list):
    lst=list
    #控制循环次数
    for i in range(0,lst.__len__()):
        #print("i",i)
        #相邻两个数据比较，大的往后放
        for j in range(0,lst.__len__()-1):
            #print("j",j)
            if lst[j]>lst[j+1]:
                #j与j+1值互换
                lst[j],lst[j+1]=lst[j+1],lst[j]
                print(lst)
if __name__ == '__main__':
    SortBy(list)