def palindrome(check):
    while len(check) > 1:
        a = check[0]
        b = check[-1]
        if a != b:
            return False
        check = check[1:-1]
#        print check
    return True


largest = 0
for a in range(999, 99, -1):
    if a*999 < largest:
        break
    for b in range(999, 99, -1):
        if palindrome(str(a*b)):
            if a*b > largest:
                largest = a*b
print largest
