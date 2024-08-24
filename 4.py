def is_palindrome(n):

    if n % 10 == 0:
        return False

    rev = 0
    while (n > 0):
        dig = n % 10
        rev = rev * 10 + dig
        n //= 10
        if n == rev:
            return True

    return False

biggest = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        if is_palindrome(i*j):
            biggest = max(biggest, i*j)

print(biggest)
