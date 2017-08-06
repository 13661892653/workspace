#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
import paramiko
private_key=paramiko.RSAKey.from_private_key_file('')
ssh =paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#拿着私钥ssh访问授权的服务器
ssh.connect(hostname='192.168.1.103',port=22,username='root',pkey='id_rsa')
stdin,stdout,stderr=ssh.exec_command('ifconfig')
result=stdout.read()
print(result.decode())
ssh.close()




