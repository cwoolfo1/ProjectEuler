def primefactor(num1):
    i = 2
    while i**2 < num1:
        while num1 % i == 0:
            num1 = num1 / i
        i = i + 1
    return num1
# this method returns the largest priime factor of a number

print("Enter a number: ")
print(primefactor(int(input())))
# takes in a integer and prints out largest prime factor