def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num = int(input("Please enter the number   :   "))

print(fibonacci(num))
