def fib(num1):
    a = 1
    b = 2
    z = 0

    x = 2

    while z < num1:
        z = a + b
        if (z%2 == 0):
            x += z
        a = b
        b = z
    return x
# method takes the even sum of the fibonacci sequence while the values are less
# than num1.
print("Enter a number: ")
num1 = int(input())
print(fib(num1))
