def sum(n):
    if n == 1:
        return n
    else:
        return sum(n-1)+n

num = int(input("Please enter a number    :     "))

print(sum(num))
