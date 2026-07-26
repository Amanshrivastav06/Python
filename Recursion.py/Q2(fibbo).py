def fibbo(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibbo(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq


print(fibbo(10))


# using function
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # update values
    return sequence


print(fibonacci(10))
