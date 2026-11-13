def fib_sequence(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq

if __name__ == "__main__":
    sequence = fib_sequence(19)
    print(sequence)

