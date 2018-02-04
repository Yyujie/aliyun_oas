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
#链接阿里云服务的配置
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
 def test_delete_archive(self):
     #选择要进行删除的目录名    
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
     try:
      for i in range(0,10000):
       archive_id=text['ArchiveList'][i]['ArchiveId']
       self.vault.delete_archive(archive_id)     
       print archive_id  +" "+'finish delete_archive'
     except IndexError,e:
	   print 'all the archive has been deleted'

t=Mession()
t.test_delete_archive()
	   
	   
	   
	   