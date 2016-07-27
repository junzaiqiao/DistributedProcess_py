#coding=utf-8


from base import QueueManagerClient


client = QueueManagerClient()(address=('192.168.200.101', 5000), authkey='secret')

client.connect()

task = client.get_task_queue()

n = 100000
for i in xrange(n):
    task.put('http://localhost:8888/?q={0}'.format(i))