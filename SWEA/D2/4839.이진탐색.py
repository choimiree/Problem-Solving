def binarySearch(lo, hi, key):
    if lo > hi: return
    mid = (lo + hi) >> 1 #비트표현
    if mid == key:
        return
    elif mid> key: #왼쪽에서 탐색
        binarySearch(lo, mid, key) + 1
    else:
        binarySearch(mid, hi, key) + 1
for tc in range(1, int(input())+1):
    p, pa, pb = map(int, input().split())
    A = binarySearch(1,p,pa)
    B = binarySearch(1,p,pb)
print('#{} {}'.format(tc, return))
'''
T=int(input())
for tc in range(1, T+1):
    temp = list(map(int, input().split()))
    result = []
    for i in range(2):
        start = 1
        end = temp[0]
        page = temp[i+1]
        cnt = 0
        while start <= end:
            mid = (start+end)//2
            if mid == page:
                break
            elif mid < page:
                start = mid
                cnt += 1
            else:
                end = mid
                cnt += 1
        result.append(cnt)

    if result[0] < result[1]:
        print('#{} A'.format(tc))
    elif result[0] > result[1]:
        print('#{} B'.format(tc))
    else:
        print('#{} 0'.format(tc))
'''