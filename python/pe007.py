from utils.my_math import Prime
from utils.main import main

def find_prime(n):
    ps = Prime()
    return ps.up_to_element(n)[-1]


if __name__ == '__main__':
    main(find_prime, 10001)
