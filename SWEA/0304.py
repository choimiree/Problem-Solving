
#장훈이의 높은선반:부분집합
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height_ls = list(map(int,input().split()))
    min = 99 #min함수를 쓰면 오래걸리기때문에, min값 정해놓고 sum이랑 비교해나가면서 바로바로 바꿔준다.
    for i in range(1, 1<<N):
        sum = 0  #여기 초기화 시켜주는 이유는 집합의 원소가 바뀔때마다 새롭게 더해줘야 하기 때문!
        for j in range(1, 1+N): #for i in range(1, 1<<N): for j in range(1, 1+N): if i & (1<<j): 이거 한 세트가 부분집합의 개수 구해주는 것!
            if i & (1<<j):
                sum += height_ls[j]
        if sum >= B and sum - B <= min:
            min = sum - B
    print('#{} {}'.format(tc, min))

#장훈이의 높은 선반: 재귀함수
def back(i,sum):
    global min_height
    if sum >= B:
        if sum <= min_height:
            min_height = sum
        return
    elif i > N-1:
        return
    else:
        back(i+1, sum)
        back(i+1, sum + height[i])
    return min_height - B

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    min_height = 100000 #최소값정해주고 선반의 높이를 빼나가다보면 최소값이 나옴. => min함수를 쓰면 오래걸리기때문에 min값을 지정해놓고 sum이랑 비교해가며 바로바로 바꿔주는 것.
    result = back(0,0) #result=back(0,0) 해주는 정확한 이유는? => 함수에서 불러와야 하니까!!
    print('#{} {}'.format(tc, result))

#수영장:재귀함수
def my_cost(k, my_sum):
    global min_cost
    if my_sum > min_cost:
        return
    if k >= 12:
        if my_sum < min_cost:
            min_cost = my_sum
        return
    if go[k] == 0:
        my_cost(k+1, my_sum)
    else:
        my_cost(k+1, cost[0]*go[k])
        my_cost(k+1, cost[1])
        my_cost(k+3, cost[2])
    return my_cost

T = int(input())
for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    go = list(map(int, input().split())) + [0] #k랑 자릿수 맞춰주려면 +[0] 해주는 거 깜빡함. 언제 판단해주는게 좋을까? => 돌려보고 range 오류나면 바꿔도 상관없음.
    min_cost = cost[3]
    my_cost(0,0)
    print('#{} {}'.format(tc, my_cost))


##[6190. 정곤이의 단조 증가하는 수]
#정곤이는 자신이 엄청난 수학자임을 증명하기 위해, 어떤 규칙 만족하는 수를 찾아보기로 했따.
#그 규칙은 단조 증가하는 수인데, 각 숫자의 자릿수가 단순하게 증가하는 수를 말한다.
#어떤 k자리 수 X=d1d2...dk가 d1<=d2<=...<=dk를 만족하면 단조 증가하는 수이다.
#예를들어 111566, 233359는 단조 증가하는 수이고, 12343, 999888은 단조 증가하는 수가 아니다.
#양의 정수 N개 A1,...,AN이 주어진다.
#1<=i<j<=N인 두 i,j에 대해, Ai x Aj 값이 단조 증가하는 수인 것들을 구하고, 그 중의 최댓값을 출력하는 프로그램을 작성하라.
#용준쓰코드
T=int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int, input().split()))
    result = -1
    for i in range(len(ls)-1):
        for j in range(i+1, len(ls)):
            a = ls[i]*ls[j]
            n = str(a)
            cnt = 0
            for x in range(len(n)-1):
                if n[x] <= n[x+1]:
                    cnt += 1
                else:
                    break
            if cnt == len(n)-1:
                if int(n) > result:
                    result = int(n)
    print('#{} {}'.format(tc, result))