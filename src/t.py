import pkg_resources

def myprint():
  print('Hi')

def sub(a,b):
  return a-b

def mytext():
  with open('docs/garbage.txt') as f:
    lines = f.readlines()
    print(lines)
  print('That is all. Thank you.')
