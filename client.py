import threading
import sys
import os
import logging
from src.image_crawler.ImageResizer import ImageResizer
from src.image_crawler.ImageDownloader import ImageDownloader
from src.utils.read_write import read
from src.models.ProducerConsumerManager import ProducerConsumerManager

LOG_FILE = 'media/download_image.log'
logging.basicConfig(
  filename=LOG_FILE,
  filemode='a',
  format='%(name)s - %(levelname)s - %(message)s',
  level=logging.INFO
)

def multi_thread(crawler: ProducerConsumerManager, resource):
  producer = threading.Thread(
    target=crawler.producer.produce,
    args=(resource, )
  )
  producer.start()

  threads = []
  for thread_id in range(crawler.numcpu):
    thread = threading.Thread(
      target=crawler.consumer.consume,
      args=(thread_id, )
    )
    thread.start()
    threads.append(thread)

  for thread in threads:
    thread.join()


def download(directory, numcpu=2, **kwargs):
  crawler = ImageDownloader(numcpu, directory)
  resource = read('media/image_urls.json')
  multi_thread(crawler, resource)


def resize(directory, numcpu=2, **kwargs):
  crawler = ImageResizer(numcpu, directory)
  resource = os.listdir(directory)
  resource = [{
    'path': f'{directory}/{e}/1_lg.jpg',
    'product_id': e,
  } for e in resource]

  multi_thread(crawler, resource)


def to_kwargs(args):
  kwargs = {}
  for arg in args:
    words = arg.split('=')
    kwargs[words[0]] = int(words[1]) if words[1].isdigit() else words[1]
  return kwargs


jobs = {
  'download': download,
  'resize': resize,
}


file, job, *args = sys.argv
fn = jobs[job]
kwargs = to_kwargs(args)

if __name__ == '__main__':
  fn(**kwargs)
