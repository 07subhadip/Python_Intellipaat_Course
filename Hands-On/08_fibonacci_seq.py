def fibonacci(num):
    sequence = []
    a, b = 0, 1

    for _ in range(num):
        sequence.append(a)
        a,b = b, a+b
    return sequence

num_of_terms = int(input("Enter the number of terms : "))
print(f"Fibonacci Sequence : {fibonacci(num_of_terms)}")