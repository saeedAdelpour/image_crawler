import abc
import queue
import logging

class IConsumer(abc.ABC):

  @abc.abstractmethod
  def consume(self, thread_id):
    pass
  
  @abc.abstractmethod
  def consume_item(self, **kwargs):
    pass




class Consumer(IConsumer):

  def __init__(self, queue: queue.Queue, directory):
    self._queue = queue
    self._directory = directory

  def consume(self, thread_id):
    while True:
      item = self._queue.get()
      if item is None:
        break
      
      self.consume_item(**item)

      logging.info('{} thread: {}, consume item: {}'.format(
        self.__class__.__name__, thread_id, str(item)
      ))