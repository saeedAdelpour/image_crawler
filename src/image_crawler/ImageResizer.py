



from src.models.Consumer import Consumer
from src.models.Producer import Producer
from src.models.ProducerConsumerManager import ProducerConsumerManager
from PIL import Image
import logging



class ImageResizerProducer(Producer):
  pass


class ImageResizerConsumer(Consumer):
  def consume_item(self, path, product_id, **kwargs):
    try:
      img_obj = Image.open(path)
      img_obj = img_obj.resize(
        [e // 2 for e in img_obj.size],
        Image.ANTIALIAS
      )
      img_obj.save(path.replace('1_lg', '1'))
    except Exception as err:
      logging.error('{}: error: {}, {}, product_id: {}'.format(
        self.__class__.__name__, err, type(err), product_id
      ))




class ImageResizer(ProducerConsumerManager):

  def __init__(self, numcpu, directory):
    super().__init__(numcpu, directory)
    self.producer = ImageResizerProducer(self.queue, numcpu)
    self.consumer = ImageResizerConsumer(self.queue, directory)