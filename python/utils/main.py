from time import time

def main(func, *args):
    start = time()
    answer = func(*args)

    print time() - start
    print answer
