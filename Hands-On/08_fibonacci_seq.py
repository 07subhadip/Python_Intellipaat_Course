# def fibonacci(num):
#     sequence = []
#     a, b = 0, 1

#     for _ in range(num):
#         sequence.append(a)
#         a,b = b, a+b
#     return sequence

# num_of_terms = int(input("Enter the number of terms : "))
# print(f"Fibonacci Sequence : {fibonacci(num_of_terms)}")


n = int(input("Enter num of terms you want : "))

if n<=0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci Sequence :")
    print("0")
elif n == 2:
    print("Fibonacci Sequence :")
    print("0, 1")
else:
    print("Fibonacci sequence:")
    a, b = 0, 1
    print(a, b, end=" ")
    count = 2
    while count < n:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        count += 1
