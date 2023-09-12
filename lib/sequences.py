# lib/sequences.py

def print_fibonacci(length):
    if length < 0:
        return []

    fibonacci_sequence = []

    for i in range(length):
        if i == 0:
            fibonacci_sequence.append(0)
        elif i == 1:
            fibonacci_sequence.append(1)
        else:
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)

    if length == 0:
        print('[]')
    else:
        print(fibonacci_sequence)

    return fibonacci_sequence
