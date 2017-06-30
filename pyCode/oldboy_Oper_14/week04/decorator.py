
import time
def timer(fun):#timer(test1)  func=test1
    def col(dd):
        print('in then col1')
        fun(dd)
        print('in then col2')
    return col

@timer# test2 = timer(test2)  = deco  test2(name) =deco(name)
def test1(name):
    time.sleep(1)
    print("in the test1",name)
test1('My')