#coding=utf-8

 
import sys
import os
sys.path.append(os.path.abspath('..'))
from base import QueueManagerClient
import time
import requests
from config import hosts
from config import log4j



class MultiprocessWork:
    __task = None
    __result = None
    
    def __init__(self):
        for i in range(len(hosts.hostsAdd['master'])):
            for k , v in hosts.hostsAdd['master'][i].iteritems():
                client = QueueManagerClient()(address=( k, v ), authkey='secret')
                
                log4j.logger.info("connect to queue...")

                client.connect()
                self.__task = client.get_task_queue()
                self.__result = client.get_result_queue()
    
    """
    利用装饰器
    """      
    @property
    def task(self):
        return self.__task
    
    @task.setter
    def task(self,task):
        self.__task = task            
    
    
    @property
    def result(self):
        return self.__result
    
#     def get_task(self):
#         return self.__task
# 
#     def set_task(self,task):
#         self.__task = task
#     
#     
#     def get_result(self):
#         return self.__result
#     
#     def set_result(self,result):
#         self.__result = result
        
        
    
def get(url):
    start = time.time()
    try:
        requests.get(url)
    except:
        ok = 0
    else:
        ok = 1
    finally:
        rt = time.time() - start
        return {'ok': ok, 'rt': rt}



if __name__=='__main__':
    muProcess = MultiprocessWork()

    while True:
        if muProcess.task.empty():
            log4j.logger.warn("no task yet, wait 5s...")
            time.sleep(5)
            continue
        try:
            i = muProcess.task.get(timeout=10)
 
            log4j.logger.warn("get {0}...".format(i))
            log4j.logger.warn("request...")
 
            o = get(i)
            muProcess.result.put({'i': i, 'o': o})
        except Exception, e:
            log4j.logger.error("Error: {0}".format(e))

        
        
        