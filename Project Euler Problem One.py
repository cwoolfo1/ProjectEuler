def multiples(num1):
    x = 0
    for i in range(num1):
        if ((i%3) == 0 or (i%5) == 0):
            x += i
    return x

# the above method takes a number and returns the sum of every multiple below
# said number

print("Enter a number: ")
num1 = int(input())

print(multiples(num1))
# takes in number and prints out the sum of all the multiples of three and five
# below that number
