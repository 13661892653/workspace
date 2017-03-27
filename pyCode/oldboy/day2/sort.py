#coding=utf-8
def sort(sortList):
    for i in range(0,sortList.__len__()-1):
        for j in range(0,sortList.__len__()-1):
            if sortList[j]>sortList[j+1]:
                sortList[j],sortList[j+1]=sortList[j+1],sortList[j]
                print(sortList)
    print(sortList)
if __name__=="__main__":
    sortList = [9999999999999,8888888, 7777777, 6666666, 55555, 44444,3333,2222,111,11,1,-4,-2]
    sort(sortList)