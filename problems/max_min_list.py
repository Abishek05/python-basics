
list = [11, 2, 34, 7, 6, 9, 13, 6]


def max_min(list):
    max = list[0]
    min = list[0]
    for num in list:
        if num > max:
            max = num
            print(max)
        elif num < min:
            min = num
            print(min)
    return min, max


max, min = max_min(list)
print(max, min)

