max_number = 10

def difference_in_squares(max_number):
    sum_of_squares = sum(i**2 for i in range(max_number + 1))
    square_of_sum = sum(i for i in range(max_number + 1))**2

    return square_of_sum - sum_of_squares

difference_in_squares(100)