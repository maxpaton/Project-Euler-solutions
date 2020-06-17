import numpy as np

answer = 0
x = 1  # Represents the current Fibonacci number being processed
y = 2  # Represents the next Fibonacci number in the sequence
while x <= 4000000:
    if x % 2 == 0:
        answer += x
    x, y = y, x + y
    
print(answer)