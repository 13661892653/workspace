import os
'''记录聊天记录哦'''
def writeFile(str):
    file='char.txt'
    isExists=os.path.exists(file)
    if not isExists:
        f = open(file, 'w')
        f.close()
    file_object = open(file, 'a')
    file_object.write(str + '\n')
    file_object.close()
if __name__=="__main__":
    while True:
        str = input("Enter your input: ")
        print("Received input is:", str)
        writeFile(str)