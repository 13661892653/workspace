#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
class people():
    age=12
    lst=[]
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def speak(self):
        print("English")
    def myForm(self):
        print('My name is:',self.name)

p1=people('chenlun','man')
p1.age=13
p1.high='175'
p1.lst.append('test')
print(p1.age,p1.lst,p1.high)
del p1.high
print(p1.age,p1.lst)
p2=people('guojuan','wuman')
print(p2.age,p2.lst)