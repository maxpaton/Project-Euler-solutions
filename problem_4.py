palindromes = []

for i in range(100, 1000):
    for j in range(100, 1000):
        number = str(i*j)
        if number == number[::-1]:  # Reverses number
            number = int(number)
            palindromes.append(number)

max(palindromes)

# or
# max(i*j for i in range(100, 1000) for j in range(100, 1000) if str(i*j) == str(i*j)[::-1])