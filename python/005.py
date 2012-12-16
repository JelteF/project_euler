def evenly_devidable1(min, max):
    output = 1
    for i in range(max, min - 1, -1):
        print i
        if output % i != 0:
            output *= i
            print output
    print output


def evenly_devidable2(min, max):
    output = 0
    while True:
        output += 20
        for i in range(max, min - 1, -1):
            if output % i != 0:
                break
        else:
            print output
            break

evenly_devidable1(1, 20)
evenly_devidable2(1, 20)
