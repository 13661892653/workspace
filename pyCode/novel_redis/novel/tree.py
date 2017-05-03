# encoding: utf-8
from PIL import Image,ImageFont,ImageDraw
import os

class dir(object):
    def __init__(self):
        self.SPACE = ""
        self.list = []

    def getCount(self, url):
        files = os.listdir(url)
        count = 0
        for file in files:
            myfile = url + "\\" + file
            if os.path.isfile(myfile):
                count = count + 1
        return count

    def getDirList(self, url):
        files = os.listdir(url)
        fileNum = self.getCount(url)
        tmpNum = 0
        for file in files:
            myfile = url + "\\" + file
            size = os.path.getsize(myfile)
            #b
            if size>1024*1024*1024:
                size = str(round(size/(1024*1024*1024),2)) + "GB"
            #Kb
            elif size>1024*1024:
                size = str(round(size/(1024*1024),2)) + "MB"
            #Mb
            elif size>1024:
                size = str(round(size/1024,2)) + "KB"
            else:
                size=str(round(size,2)) +"B"
            if os.path.isfile(myfile):
                tmpNum = tmpNum + 1
                if (tmpNum != fileNum):
                    self.list.append(str(self.SPACE) + "├─" + file + "    " + str(size)+ "\n")
                else:  # www.iplaypy.com
                    self.list.append(str(self.SPACE) + "└─" + file + "    " + str(size)+ "\n")

            if os.path.isdir(myfile):
                self.list.append(str(self.SPACE) + "├─" + file + "\n")
                # change into sub directory
                self.SPACE = self.SPACE + "│  "
                self.getDirList(myfile)
                #print(self.getDirList(myfile))
                # if iterator of sub directory is finished, reduce "│  "
                self.SPACE = self.SPACE[0:-3]
        return self.list

    def writeList(self, url):
        f = open(url, 'w')
        f.writelines(self.list)
        print("ok")
        f.close()
        #im.save("1.1.jpg")


if __name__ == '__main__':
    d = dir()
    #树状显示目录结构以及文件的大小，更改以下路径即可
    HomeDir="E:\\svn"#更改这个地方即可
    d.getDirList(HomeDir)  # input directory
    d.writeList("1.txt")  # write to file