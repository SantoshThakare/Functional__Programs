def triples(arr, num):
    sum = 0
    for i in range(0, num):
        for j in range(i + 1, num):
            for k in range(j + 1, num):
                sum = arr[i] + arr[j] + arr[k]

                if sum == 0:
                    print("arr[i]", arr[i], " arr[j] ", arr[j], " arr[k] ", arr[k])

    if sum != 0:
        print("triplet is not exist")

if __name__ == '__main__':
    arr = [0, -1, 2, -3, 1]
    num = len(arr)
    triples(arr, num)