#coding=utf-8

def main(age,amt):
    if age==50:
        print("折扣%s：,折扣后金额%s"%(9.5,amt * 0.95))
    else:
        if amt>=100000:
            print("折扣%s：,折扣后金额%s" % (9, amt * 0.9))
        elif amt>=80000:
            print("折扣%s：,折扣后金额%s" % (9.5, amt * 0.95))
        elif amt>=50000:
            print("折扣%s：,折扣后金额%s" % (9.8, amt * 0.98))
        else:
            print("不满足打折条件")
if __name__=="__main__":
    age=int(input("消费者年龄："))
    amt=int(input("消费金额："))
    main(age,amt)
