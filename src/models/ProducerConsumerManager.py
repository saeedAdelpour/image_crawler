from src.utils.functions import my_mkdir
from src.models.Producer import Producer
from src.models.Consumer import Consumer
import queue


class ProducerConsumerManager:

  consumer: Consumer
  producer: Producer

  QUEUE_SIZE = 100

  def __init__(self, numcpu, directory):
    self.numcpu = numcpu
    self.queue = queue.Queue(self.QUEUE_SIZE)
    my_mkdir(directory)
