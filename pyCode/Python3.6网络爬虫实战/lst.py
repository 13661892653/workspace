#coding=utf-8
#author:colby

class Student(object):
    def __init__(self,name,sex,age,height):
        self.name=name
        self.sex=sex
        self.age=age
        self.height=height

    def printInfo(self):
        print(self.name,self.sex,self.age,self.height)

def main():
    s1=Student("colby","man","20","70Kg")
    s1.printInfo()

if __name__ == "__main__":
    main()
