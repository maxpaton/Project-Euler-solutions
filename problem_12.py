def compute():
    triangle = 0
    for i in itertools.count(1):
        # Keeps running total of triangle numbers (adds natural number each iteration)
        triangle += i
        if find_divisors(triangle) > 500:
            return 'Triangle number: {}'.format(triangle)

# For each triangle number, we call this function to get the number of divisors
def find_divisors(n):
    # Set gets unique values from 'k' and 'triangle//k'
    # Only go up to sqrt(n) as we are obtaining n//k (the larger corresponding factor) as well as k
    divisors = set(reduce(list.__add__, 
            [[j, n//j] for j in range(1, int(n**0.5) + 1) if n % j == 0]))
    return len(divisors)
    
        
if __name__ == '__main__':
    print(compute())