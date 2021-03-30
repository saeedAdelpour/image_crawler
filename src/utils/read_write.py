import json

def read(directory):
  with open(directory) as fp:
    data = json.load(fp)
  return data


def write(data, directory):
  with open(directory, encoding='utf-8') as fp:
    json.dump(data, fp)
