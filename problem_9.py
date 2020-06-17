def compute():
    for i in range(1, 1000):
        for j in range(i+1, 1000):
            c = 1000 - i - j
            if i*i + j*j == c*c:
                return i*j*c

compute()