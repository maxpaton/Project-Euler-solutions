x = 600851475143
# x = 15


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(2, x+1):
    if is_prime(i) and x % i == 0:
        print(i)