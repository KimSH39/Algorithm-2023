import sys
input = sys.stdin.readline
n, k = map(int, input().split())
list = list(map(int, input().split()))

def insertion_sort(list):
    n=len(list)
    count = 0
    result = -1

    for i in range(1, n):
        loc = i-1
        newItem = list[i]
        while 0<= loc and newItem < list[loc]:
            list[loc+1] = list[loc]
            loc -=1
            count += 1
            if count == k:
                result = list[loc+1]

        if loc+1 != i:
            list[loc+1] = newItem
            count +=1
            if count == k:
                result = list[loc+1]

    print(result)

insertion_sort(list)