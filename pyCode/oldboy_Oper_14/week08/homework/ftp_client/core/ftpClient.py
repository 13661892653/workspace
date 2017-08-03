#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:
__author__ = "Colby"
import socket
import os
import json

class ftpClient(object):
    def __init__(self):
        self.client=socket.socket()
    def help(self):
        msg = '''
        ls
        pwd
        cd ../..
        get filename
        put filename
        '''
        print(msg)
    def connect(self,ip,port):
        self.client.connect((ip,port))
    def start(self):
        while True:
            cmd = input("发送数据#")
            if len(cmd) == 0: continue
            cmdStr=cmd.split()[0]
            if hasattr(self,'client%s' %cmdStr):
                action=getattr(self,'client%s' %cmdStr)
                '''
                如果输入的命令合法，能够找到对应的处理函数，那么
                就调用函数
                clientget(get filename)
                '''
                action(cmd)
            else:
                continue
    def clientput(self,*args):
        cmdSplit=args[0].split()
        if len(cmdSplit)>1:
            filename=cmdSplit[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                mydict = {
                    'action': 'put',
                    'filename': filename,
                    'filesize': filesize
                }
                self.client.send(json.dumps(mydict).encode("utf-8"))
                server_response=self.client.recv(1024)
                print('server_response:',server_response)
                f=open(filename,'rb')
                send_size=0
                for line in f:
                    self.client.send(line)
                    send_size+=len(line)
                    process=int(float(send_size)/float(filesize)*100)
                    print('='*(int(process/5)),process,'%')
                else:
                    print('文件%s发送ok' % filename )
                    f.close()
            else:
                print('%s文件不存在' %filename)
    def clientget(self):
        pass
    def clientls(self):
        pass
    def clientcd(self):
        pass
    def clientpwd(self):
        pass

if __name__=='__main__':
    #实例化对象
    ftp1=ftpClient()
    ftp1.connect('localhost',10002)
    ftp1.start()