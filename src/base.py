#coding=utf-8

from multiprocessing.managers import BaseManager

class _QueueManagerServer(BaseManager):
    pass


def QueueManagerServer(task_queue, result_queue):
    _QueueManagerServer.register('get_task_queue', callable=lambda: task_queue)
    _QueueManagerServer.register('get_result_queue', callable=lambda: result_queue)
    return _QueueManagerServer


class _QueueManagerClient(BaseManager):
    pass

def QueueManagerClient():
    _QueueManagerClient.register('get_task_queue')
    _QueueManagerClient.register('get_result_queue')
    return _QueueManagerClient