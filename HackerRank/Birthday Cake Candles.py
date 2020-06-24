def birthdayCakeCandles(ar):
    count=0
    ar.sort()
    le=len(ar)
    maxv=ar[le-1]
    for i in ar:
        if i==maxv:
            count+=1
    print(count)
if __name__ == '__main__':

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
