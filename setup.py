from setuptools import setup

def readme():
    with open('garbage.txt') as f:
        return f.read()

setup(
  long_description=readme(),
  include_package_data=True)
