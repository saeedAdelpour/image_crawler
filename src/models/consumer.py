import abc
import queue

class IConsumer(abc.ABC):

  @abc.abstractmethod
  def consume(self, _queue):
    pass
  
  @abc.abstractmethod
  def consume_item(self, item):
    pass




class Consumer(IConsumer):

  def __init__(self, queue: queue.Queue):
    self._queue = queue

  def consume(self):
    while True:
      item = self._queue.get()
      if item is None:
        break
      
      self.consume_item(item)