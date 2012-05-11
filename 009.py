for a in range(1, 1000):
    for b in range(a, 1000-a):
        c = 1000 - a - b
        if (a**2 + b**2) == c**2:
            print a
            print b
            print c
            print a*b*c
