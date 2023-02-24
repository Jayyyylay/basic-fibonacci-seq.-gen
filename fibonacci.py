def fibonacci(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, num):
            next_fib = fib_sequence[i-1] + fib_sequence[i-2]
            fib_sequence.append(next_fib)
        return fib_sequence
again = True
while again:
    num = int(input("Please input how long is the sequence: "))
    output = fibonacci(num)
    print(output)