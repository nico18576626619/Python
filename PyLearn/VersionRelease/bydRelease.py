# -*- coding: UTF-8 -*-
import paramiko
import logging
import sys
logging.basicConfig(filename='Release.log', filemode="w", level=logging.INFO)
hostname='192.168.1.102'
username='root'
password='123456'
port=22
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname,port, username, password, timeout=4)

# 上传文件
def sftp_upload_file(server_path, local_path):
    try:
        t = paramiko.Transport((hostname, 22))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_path, server_path)
        logging.info('从{}上传文件到{}成功'.format(local_path, server_path))
        t.close()
    except Exception as e:
        logging.info('上传失败',e)


# 是否存在子字符串
def isInList(list,key):
    for i in list:
        if key in str(i):
            return True
    return False

# 进程是否存在
def existProgress(client,progressname,progressKey):
    try:
        cmd='ps -ef|grep '+progressname
        # print(cmd)
        stdin, stdout, stderr = client.exec_command(cmd)
        list=stdout.read().splitlines()
        if isInList(list,progressKey):
            logging.info('{}进程存在'.format(progressKey))
            return True
        else:
            logging.info('{}进程不存在'.format(progressKey))
            return False
    except Exception as e:
        logging.info('查看线程失败', e)

# 删除文件
def deleteFile(client,regular):
    try:
        cmd = 'rm -rf '+regular
        stdin, stdout, stderr = client.exec_command(cmd)
        logging.info('删除{}成功'.format(regular))
    except Exception as e:
        logging.info('删除失败',e)

# 文件是否存在
def fileIsExsit(client,regular):
    cmd = 'find /home/nico -name ' + regular
    stdin, stdout, stderr = client.exec_command(cmd)
    temp=str(stdout.read(),encoding = "utf-8")
    if temp==''or temp==None:
        logging.info('{}文件存在'.format(regular))
        return True
    else:
        logging.info('{}文件不存在'.format(regular))
        return False

if __name__=='__main__':
    if fileIsExsit(client, '1*'):
        deleteFile(client, '1.txt')
        sftp_upload_file('/home/nico/1.txt','1.txt')
    logging.info('---------------------------')


