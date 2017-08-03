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
                for line in f:
                    self.client.send(line)
                    try:
                        total_size=self.client.recv(1024)
                        receive_size=0
                        received_data=b''
                        while receive_size < int(total_size.decode()):
                            data = self.client.recv(1024)
                            receive_size += len(data)  # 每次收到的有可能小于1024，所以必须用len判断
                            # print(data.decode())
                            received_data += data
                        else:
                            print('receive:', receive_size)
                            received_data=int(received_data.decode())
                            print('=' * received_data, received_data, '%')

                    except ValueError as e:
                        print(e)
                        continue
                else:
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