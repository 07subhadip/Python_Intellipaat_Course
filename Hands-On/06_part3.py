num = int(input("Enter a number :"))

if num < 2:
    print(f"{num} is not a Prime Number")
else:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a Prime Number")
            break
    else:
        print(f"{num} is a Prime Number")