# Check for armstrong or not
def is_armstrong(num):
    digit = str(num)
    power = len(digit)
    total = sum(int(d) ** power for d in digit)
    return total == num

num = int(input("Enter a number :"))

if  is_armstrong(num):
    print(f"{num} is Armstrong")
else:
    print(f"{num} is not Armstrong")