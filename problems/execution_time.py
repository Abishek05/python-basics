from timeit import default_timer


def timer(num):
    # starting point
    start = default_timer()
    for i in range(0, num):
        print(i)
    # End point
    end = default_timer()
    print(start-end)


timer(400)
