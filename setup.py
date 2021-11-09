from setuptools import setup

def readme():
    with open('garbage.txt') as f:
        l = f.read()
        print(l)
        return l

setup(include_package_data=True)
