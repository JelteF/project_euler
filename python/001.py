import time

""" Add all the natural numbers below one thousand
that are multiples of 3 or 5.
"""

def using_union():
    three = range(3, 1000, 3)
    five = range(5, 1000, 5)
    return sum(set().union(three, five))

def using_iteration():
    sum_ = 0

    for i in range(3, 1000, 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_ += i

    return sum_

start = time.time()
sum_ = using_union()
print (time.time() - start)
print sum_

start = time.time()
sum_ = using_iteration()
print (time.time() - start)
print sum_
