def InsertAt(S, idx, num):
    global NL
    if S == 'I':
        NL = NL[:idx] + [num] + NL[idx::]
    else:
        NL[idx] = num

for tc in range(1, int(input())+1):
    N, M, L = map(int, input().split())
    NL = list(map(int, input().split()))
    for i in range(M):
        Put = input().split()
        if Put[0] == 'D':
            NL = NL[:int(Put[1])] + NL[int(Put[1])+1::]
        else:
            InsertAt(Put[0], int(Put[1]), int(Put[2]))

    if len(NL) <= L:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc, NL[L]))