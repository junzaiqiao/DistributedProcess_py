#coding=utf-8

__PATH__="/home/ocdc/DistributedProcess_py"

import sys
sys.path.append(__PATH__)
from base import QueueManagerServer
from multiprocessing import Queue
from multiprocessing import freeze_support
from config import hosts
from config import log4j

task_queue = Queue()
result_queue = Queue()

Server = QueueManagerServer(task_queue, result_queue)

for i in range(len(hosts.hostsAdd['master'])):
    for k , v in hosts.hostsAdd['master'][i].iteritems():
        manager = Server(address=(k , v), authkey='secret')
   
#         server = manager.get_server()

#         server.serve_forever()

        manager.start()
        log4j.logger.info("Server is running...")

        manager.join()
        
    
        