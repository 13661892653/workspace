#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import paramiko
ssh =paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.1.103',port=22,username='root',password='jk20ac')
stdin,stdout,stderr=ssh.exec_command('ifconfig')
result=stdout.read()
print(result.decode())
ssh.close()
