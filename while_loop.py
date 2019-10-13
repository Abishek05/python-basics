check = True

count = 0
while check == True:
    count += 1
    if count == 3:
        check = False
    print("Check is true")


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while list[0] != 10:
    list.remove(list[0])
    print(list)
