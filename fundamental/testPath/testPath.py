import os


def createPath():
    print(f"inner... {os.path.dirname(__file__)}")
    return os.path.dirname(__file__)
