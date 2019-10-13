a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))

remainder = a % b

if remainder == 0:
    print("{} is divisible by {}".format(a, b))
else:
    print("{} is not divisible by {}".format(a, b))

