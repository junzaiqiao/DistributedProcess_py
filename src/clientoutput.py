# -*- coding: utf-8 -*-


from base import QueueManagerClient
import time


client = QueueManagerClient()(address=('192.168.200.101', 5000), authkey='secret')

client.connect()

result = client.get_result_queue()


while True:
    if result.empty():
        print 'no result yet, wait 5s'
        time.sleep(5)
        continue
    try:
        print result.get(timeout=2)
    except Exception as e:
        print 'Error: {0}'.format(e)