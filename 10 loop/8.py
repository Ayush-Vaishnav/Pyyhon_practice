#check if a number is prime number

n = int(input("Enter number: "))

is_prime = True

if n >1:
    for i in range(2, n):
        if (n %i) == 0:
            is_prime = False
            break

print(is_prime)