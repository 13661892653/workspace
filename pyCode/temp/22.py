#coding="utf-8"
lst=[1,1,0,2,2,2,4,3,3,4,2,0,0]
resultList=[]
middleList=['']
j=''
for i in lst:
    if i==middleList[-1]:
        middleList.append(i)
    else:
        middleList=[]
        middleList.append(i)
        resultList.append(middleList)
print(resultList)