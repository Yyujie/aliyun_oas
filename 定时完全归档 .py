# coding=utf-8 
#!/usr/bin/python
import demjson
import shutil
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
#实现从OSS中的'seimport-test'归档到OAS中的'work'目录下
class Mession():
 def __init__(self):
  self.api = OASAPI(conf.host, conf.accesskey_id, conf.accesskey_secret)
  self.vault = Vault.create_vault(self.api, conf.vault_name )
  self.auth = oss2.Auth(conf.accesskey_id, conf.accesskey_secret)
  self.bucket = oss2.Bucket(self.auth,self.osshost, config.bucket)
 def test_pull_from_oss(self): 
  #控制归档Object条件，时间“七天内”，个数   
  for obj in oss2.ObjectIterator(self.bucket, prefix='文件前缀'):
   t=int(time.time()-obj.last_modified)    
   if (t > 604800):                    
     job = self.vault.pull_from_oss(conf.osshost, conf.bucket, obj.key)
     print(obj.key)	 
     self.bucket.delete_object(obj.key)	
  print 'finish push to oas'
  
t=Mession()
t.test_pull_from_oss()