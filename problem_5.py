# This can be done using a for loop in steps on 20, since we know the number has to be divisible by 20
# This saves a lot of time!

max_divisor = 20
divisors = range(1, max_divisor+1)

for i in range(max_divisor, 99999999999999, max_divisor):
    if all(i % divisor == 0 for divisor in divisors):
        print(i)
        break