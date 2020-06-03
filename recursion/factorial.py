def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n
num = int(input("Enter a number to get factorial of it    :     "))

print(fact(num))
