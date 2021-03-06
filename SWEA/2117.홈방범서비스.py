'''
N*N 크기의 도시에 홈방법 서비스를 제공하려고 한다.
홈방범 서비스는 운영상의 이유로 마름모 모양의 영역에서만 제공된다.
또한, 홈방범 서비스를 제공하기 위해 운영 비용이 필요하다.
서비스 영역의 크기 K가 커질수록 운영 비용이 커진다.
운영 비용은 서비스 영역의 면적과 동일하며, 아래와 같이 구할 수 있다.
운영 비용 = K*K + (K-1)*(K-1)
운영 영역의 크기 K는 1이상의 정수이다.
홈방범 서비스를 제공받는 집들은 각각 M의 비용을 지불할 수 있어, 보안회사에서는 손해를 보지 않는 한 최대한 많은 집에 홈방범 서비스를 제공하려 한다.
도시의 크기 N과 하나의 집이 지불할 수 있는 비용 M, 도시의 정보가 주어진다.
이때, 손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고, 그 때의 홈방범 서비스를 제공 받는 집들의 수를 출력하는 프로그램을 작성하라.
[제약]
최대 50개 테스트 케이스.
N은 5이상 20이하 정수.
하나의 집이 지불할 수 있는 비용 M은 1이상 10이하의 정수.
홈방범 서비스의 운영 비용은 서비스 영역의 면적과 동일.
도시의 정보에서 집이 있는 위치는 1이고, 나머지는 0이다.
도시에서 최소 1개 이상의 집이 존재.
[출력]
집의 수
[접근 방법]
- NxN의 모든 칸을 서비스 영역의 중심으로 고려한다.
- K값을 바꿔가며, 손해가 나지 않는 최대 집 수를 확인한다.
	- K의 범위를 정한다.
	- K에 대한 서비스 비용을 미리 계산해 둔다.
	- K가 큰 경우부터 고려한다/K가 작은 경우부터 고려한다.
- 집 1개 이상, 지불 가능 비용 M >= 1, K >= 1이므로, 서비스 가능한 최대 집의 수(minV) >= 1
- N에 대한 K의 최대값 (NxN영역을 모두 포함하는 경우)
	- N=2일 때, K<=3. N=3일때 K<=3
- 모든 칸에 대해 K=1 부터 K=N+1까지,
서비스 가능한 집 수*부담비용(M) <= K*K+(K-1)*(K-1)을 만족하는,
서비스 가능한 최대 집 수를 알아본다.
but, 시간이 오래 걸린다.
- 모든 칸의 좌표 i,j를 중심으로 모든 집과의 거리 d를 계산
- 집의 좌표가 p,q라면,
거리별 집의 수를 기록한 cnt 배열 초기화.
모든 칸의 좌표 i,j에 대해,
모든 집의 좌표 p,q에 대해
d=abs(i-p)+abs(j-q)+1
cnt[d]
- cnt 배열을 거리순으로 누적해 거리 k이내의 집 수를 기록
for K:1 -> N+1
cnt[K] = cnt[K] + cnt[K-1]
- 모든 거리 K에 대해,
cnt[K] * 부담 비용(M) <= K*K + (K-1)*(K-1) 조건을 만족하는 K의 최대값을 찾는다.
'''
import sys
sys.stdin = open("2117.txt","r")

cost = [K*K+(K-1)*(K-1) for K in range(22)] #K대비 비용, 최대 N+1=21
T=int(input())
for tc in range(1,T+1):
    # cnt = 0
    N,M=map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    home = []
    ans = 0
    #마름모의 중심
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                home.append((i,j))

    cnt = [0]*(N+2) #i,j를 중심으로 거리 +1이 K인 집의 개수 기록
    # k별 집의 수
    for p,q in home:    #모든 집과의 거리 기록
        dis = abs(i-p) + abs(j-q) + 1   #i,j와 집이 같으면 K가 1
        if dis <= N+1:
            cnt[dis] += 1
    # k이내의 집의 수
    for k in range(1, N+2):
        cnt[k] += cnt[k-1]
        if cnt[k]*M >= cost[k]: #방범 구역 설정에 손해가 아니면
            if ans<cnt[k]:
                ans = cnt[k]

    print('#{} {}'.format(tc, ans))
