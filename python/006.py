one = 0
for a in range(1, 101):
    one += a**2
two = 0
for a in range(1, 101):
    two += a
two = two**2
print two - one
