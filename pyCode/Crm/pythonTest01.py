#coding=utf-8

def main():
    while True:
        string = input("请输入字符：")
        if string.isdigit():
            print("数字")
        elif string.isupper():
            print("大写字母")
        elif string.islower():
            print("小写字母")
        else:
            print("特殊字符")

if __name__=="__main__":
    main()
