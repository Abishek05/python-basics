for elements in range(1, 10):
    print(elements)


count = 0
for i in range(1, 5):
    count += 1
print(count)


# to print numbers greater than 4 from a list
list = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 12, 16, 19, 3, 4, 5]
number = 4

for i in list:
    if i > number:
        print(i)
        