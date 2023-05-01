array = [1, 3, 5, 7, 9, 10]


def middleelement(arr):
    halfway = len(arr) // 2
    print (arr[halfway])
    if len(arr) % 2 != 0:
        print(arr[halfway])
    else:
        print(arr[halfway - 1], arr[halfway])

middleelement(array)
