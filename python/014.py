sequenceLength = [0]
maximum = 0
highest = 0
for a in range(1, 1000000):
    n = a
    sequenceLength.append(1)
    while n > 1:
        if n % 2 == 0:
            n /= 2
            sequenceLength[a] += 1
        else:
            n = 3*n+1
            sequenceLength[a] += 1
        if len(sequenceLength) > n:
            sequenceLength[a] += sequenceLength[n] - 1
            break
    if maximum < sequenceLength[a]:
        maximum = sequenceLength[a]
        highest = a
print highest
