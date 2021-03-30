import os


def my_mkdir(directory):
  dirs = directory.split("/")
  for i in range(len(dirs)):
    try:
      os.mkdir("/".join(dirs[:i+1]))
    except:
      pass