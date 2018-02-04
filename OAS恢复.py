# coding=utf-8 
#!/usr/bin/python
import demjson
import os
import oss2 
import datetime
import time
from itertools import islice 
from oas.oas_api import OASAPI
from oas.ease.vault import Vault
#链接阿里云服务的配置,根据自己的bucket和秘钥信息填写
class Conf(object):

    def __init__(self):	   
        self.host = 'cn-hangzhou.oas-internal.aliyuncs.com'
        self.accesskey_id = ''
        self.accesskey_secret = ''
        self.vault_name = ''        				
        self.osshost = 'oss-cn-hangzhou-internal.aliyuncs.com'
        self.bucket = ''		

conf = Conf() 

class Mession():
 def __init__(self):
  self.api = OASAPI(conf.host, conf.accesskey_id, conf.accesskey_secret)
  self.vault = Vault.create_vault(self.api, conf.vault_name )
  self.auth = oss2.Auth(conf.accesskey_id, conf.accesskey_secret)
  self.bucket = oss2.Bucket(self.auth,self.osshost, config.bucket)
 def test_push_to_oss(self):
     #选择要进行恢复的目录名'测试用oascmd-test'		 
     m=raw_input('please choose a vault:  ') 	 
     self.vault = Vault.get_vault_by_name(self.api, m)
     f = open('D:/test.txt','w')	 
     job = self.vault.retrieve_inventory()     		 
     job.download_to_file('D:/test.txt')
     f = open('D:/test.txt') 
     arr=[]	 
     line = f.readline()             
     while line:   
       arr.append(line)
       line = f.readline()
     f.close()
     str = ('').join(arr)
     text = demjson.decode(str) 
     list=[]
	 #选择要恢复的文件名字
     n=raw_input('please input a name:  ')	 
     try:
      for i in range(0,10000):
       objname=text['ArchiveList'][i]['ArchiveDescription']     #sepop-dev/1111111
       list.append(objname)      	            
     except IndexError,e:
       j=list.index(n)
       archive_id=text['ArchiveList'][j]['ArchiveId']
       job = self.vault.retrieve_archive(archive_id)
       job.download_to_file('D:/test1.txt')
       with open('D:/test1.txt',"r") as f:
               content=f.readlines()
       print content
       #由文件所对应内容再次确认是否恢复	   
       k=int(raw_input('if you want to continue:1 or 0:  '))	
       if (k==1):	   
        job = self.vault.push_to_oss(archive_id, conf.osshost, conf.bucket, archive_id)
        print job	   
        print n  +" "+'finish push to oss'
        exit()		
       elif (k==0):
	    print 'please input again'
	   			  	 
t=Mession()
while(True):
 t.test_push_to_oss()



