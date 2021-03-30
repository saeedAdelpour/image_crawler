import requests
import shutil
from src.utils.functions import my_mkdir
from src.models.Consumer import Consumer
from src.models.Producer import Producer
from src.models.ProducerConsumerManager import ProducerConsumerManager
import logging


class ImageDownloaderProducer(Producer):
  pass



class ImageDownloaderConsumer(Consumer):

  def consume_item(self, url, product_id, **kwargs):
    try:
      img_directory = f'{self._directory}/{product_id}'
      my_mkdir(img_directory)
      response = self._get_response(url)
      self._save_lg(img_directory, response)
    except Exception as err:
      logging.error('{}: error: {}, {}, product_id: {}'.format(
        self.__class__.__name__, err, type(err), product_id)
      )


  def _get_response(self, url):
    response = requests.get(url=url, stream=True)
    return response

  def _save_lg(self, directory, response):
    response.raw.decode_content = True
    with open(f'{directory}/1_lg.jpg', 'wb') as fp:
      shutil.copyfileobj(response.raw, fp)    
    




class ImageDownloader(ProducerConsumerManager):
  
  def __init__(self, numcpu, directory):
    super().__init__(numcpu, directory)
    self.producer = ImageDownloaderProducer(self.queue, numcpu)
    self.consumer = ImageDownloaderConsumer(self.queue, directory)

  