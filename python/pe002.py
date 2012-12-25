from utils.my_math import Fibonacci
from utils.main import main

"""
Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

def even_fibonaci_sum(max_fib):
    f = Fibonacci()
    fibo_numbers = f.up_to(max_fib)
    return sum(fibo_numbers[2::3])  #Every third number in the sequence is even


if __name__ == '__main__':
    main(even_fibonaci_sum, 4e6)