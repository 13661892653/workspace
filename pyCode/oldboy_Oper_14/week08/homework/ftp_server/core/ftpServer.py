#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:2017-08-02
__author__ = "Colby"
import json
import os
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def put(self,*args):
        self.request.send(b'ok')
        # print('receive,filename,filesize:',filename,filesize)
        cmdDict=args[0]
        filename = cmdDict['filename']
        filesize = cmdDict['filesize']
        if os.path.isfile(filename):
            f = open(filename + ".new", "wb")
        else:
            f = open(filename, "wb")
        received_size = 0
        # print('received_size,filesize',received_size,filesize)
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print("file [%s] has uploaded..." % filename)
            self.request.send(str(100).encode('utf-8'))
    def get(self,*args):
        print('server get command!')
        getmydict=args[0]
        filename=getmydict['filename']
        if os.path.isfile(filename):
            print('存在此文件%s' %filename)
            self.request.send(('存在此文件%s' %filename).encode('utf-8'))
        else:
            print('不存在此文件%s' %filename)
            self.request.send(('不存在此文件%s' %filename).encode('utf-8'))
    def ls(self,*args):
        pass
    def cd(self,*args):
        pass
    def pwd(self,*args):
        pass
    def help(self):
        print('''
        -------------------
            ls file/path
            cd ../path/dir
            pwd
            help()
            put file
            get file
        --------------------
        ''')
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print(self.data)
                cmd_dic = json.loads(self.data.decode())
                actionStr=cmd_dic['action']
                if hasattr(self,actionStr):
                    action=getattr(self,actionStr)
                    action(cmd_dic)
            except ConnectionResetError as e:
                print("err",e)
                break
if __name__ == "__main__":
    HOST, PORT = "localhost", 10002
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
