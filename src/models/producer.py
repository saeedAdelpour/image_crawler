import abc
import queue

class Iproducer(abc.ABC):

  @abc.abstractmethod
  def produce(self, resource):
    pass


class Producer(Iproducer):

  def __init__(self, queue: queue.Queue, numcpu):
    self._queue = queue
    self._numcpu = numcpu
    self._poisen_pill = None
  
  def produce(self, resource):
    for resource_item in resource:
      self._queue.put(resource_item)
    
    for _ in range(self._numcpu):
      self._queue.put(self._poisen_pill)


