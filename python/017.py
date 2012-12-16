def generate_size(start, size, fromm, tto, numbers):
    for a in range(fromm, tto):
        numbers[start + a] = size + numbers[a]


size = 1001
numbers = [0]*size
numbers[0] = 0
numbers[1] = len("one")
numbers[2] = len("two")
numbers[3] = len("three")
numbers[4] = len("four")
numbers[5] = len("five")
numbers[6] = len("six")
numbers[7] = len("seven")
numbers[8] = len("eight")
numbers[9] = len("nine")
numbers[10] = len("ten")
numbers[11] = len("eleven")
numbers[12] = len("twelve")
numbers[13] = len("thirteen")
for a in range(4, 10):
    numbers[10 + a] = 4 + numbers[a]
numbers[15] = len("fifteen")
numbers[18] = len("eighteen")
generate_size(20, len("twenty"), 0, 10, numbers)
generate_size(30, len("thirty"), 0, 10, numbers)
generate_size(40, len("forty"), 0, 10, numbers)
generate_size(50, len("fifty"), 0, 10, numbers)
for a in range(60, 100, 10):
    generate_size(a, numbers[a/10] + len("ty"), 0, 10, numbers)
generate_size(80, len("eighty"), 0, 10, numbers)
for a in range(100, 1000, 100):
    numbers[a] = numbers[a/100] + len("hundred")
    generate_size(a, numbers[a/100] + len("hundred") + len("and"), 1, 100, numbers)
numbers[1000] = len("onethousand")

total = 0
counter = 0
for a in numbers:
    print counter, a
    total += a
    counter += 1
print total
