#!/usr/bin/env python

def read_dict(name):
  """Returns the set of words in the dictionary <name>.dict."""
  out = set()
  with open(name + '.dict') as file:
    for line in file:
      out.add(line.split()[0].lower())
  return out

if __name__ == '__main__':
  words = read_dict('british')
  print('test' in words)
