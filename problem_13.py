filename = './13_number.txt'

def get_sum():
    with open(filename, 'r') as f:
        array = [line for line in f]

        # Convert list of strings to list of numbers
        int_array = [int(line) for line in array]

    total = sum(int_array)
    return str(total)[:10]

if __name__ == '__main__':
    print(get_sum())