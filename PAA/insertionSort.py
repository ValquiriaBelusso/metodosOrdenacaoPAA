from math import floor
import time


def currentTimeMillis():
    return time.time() * 1000


def insertionSort(arr):
    start = currentTimeMillis()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    totalTime = currentTimeMillis() - start
    return str(totalTime)


def insertionBucket(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucketSort(arr, b):
    start = currentTimeMillis()
    n = len(arr)
    buckets = [[] for y in range(b)]
    sorted = []

    max = 0
    for i in range(0, n):
        if (arr[i] > max):
            max = arr[i]

    for i in range(0, n):
        pos = floor(b*arr[i] / max)
        if (pos == b):
            buckets[b-1].append(arr[i])
        else:
            buckets[pos].append(arr[i])

    for bucket in buckets:
        insertionBucket(bucket)
        sorted.extend(bucket)
    totalTime = currentTimeMillis() - start
    return str(totalTime)


numberOfBuckets = [0, 10, 50, 100, 1000]
types = ["a", "d", "o", "po"]
sampleSize = [100, 200, 500, 1000, 2000, 5000, 7500, 10000, 15000, 30000, 50000,
              75000, 100000, 200000, 500000, 750000, 1000000, 1250000, 1500000, 2000000]

for i in range(0, 3):
    for b in numberOfBuckets:
        for type in types:
            for size in sampleSize:
                with open(
                        "{type}/{sampleSize}.txt".format(type=type, sampleSize=size), "r") as source:

                    arr = []
                    for n in source:
                        arr.append(int(n))

                    with open("Resultados/{b}/{type}{size}.txt".format(b=b, type=type, size=size), "a") as res:
                        if (b == 0):
                            res.write(insertionSort(arr))
                        else:
                            res.write(bucketSort(arr, b))
                        res.write("\n")
