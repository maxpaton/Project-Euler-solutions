def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

sum(i for i in range(2, 2000000) if is_prime(i))