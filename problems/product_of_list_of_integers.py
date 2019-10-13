
list = [1, 2, 3, 4]

product = 1

while len(list) > 0:
    product = product * list[0]
    list.remove(list[0])
print(product)
