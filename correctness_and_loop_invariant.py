def insertionSort(N, arr):
    for i in range (1,N):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = value

    for j in range (0,N):
        print(arr[j], end=" ")

N = int(input())
arr = [int(x) for x in input().split()]

insertionSort(N, arr)

