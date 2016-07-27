#coding=utf-8

__PATH__="/home/ocdc/DistributedProcess_py"
 
import sys
sys.path.append(__PATH__)
from base import QueueManagerClient
import time
import requests
from config import hosts
from config import log4j



class MultiprocessWork:
    task = None
    result = None
    
    def __init__(self):
        for i in range(len(hosts.hostsAdd['master'])):
            for k , v in hosts.hostsAdd['master'][i].iteritems():
                client = QueueManagerClient()(address=( k, v ), authkey='secret')
                
                log4j.logger.info("connect to queue...")

                client.connect()
                MultiprocessWork.task = client.get_task_queue()
                MultiprocessWork.result = client.get_result_queue()
    
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

        
        
        