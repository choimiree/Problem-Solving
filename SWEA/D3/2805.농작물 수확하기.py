#NxN크기의 농장이 있다.
#이 농장에는 이상한 규칙이 있다.
#규칙은 다음과 같다.
#1) 농장은 크기는 항사 홀수이다.(1x1, 3x3,,49x49)
#2) 수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능하다.
#1x1 크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 3이다.
#3x3 크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 16(3+2+4+2)
#5x5 크기의 농장에서 자라는 농작물을 수확하여 얻을 수 있는 수익은 25(3+2+1+1+2+5+1+1+3+3+2+1)
#농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.
#농장의 크기 N은 1이상 49이하의 홀수이다.
#농작물의 가치는 0~5이다.
for tc in range(1, int(input())+1):
    N=int(input())
    arr = [input().strip() for _ in range(N)]    # 입력을 문자열 배열로 처리 #strip()은 생략가능

    s = e = N//2
    ans=0
    for row in range(N):
        for i in range(s, e+1):
            ans += int(arr[row][i])         # 문자열이니까 정수로 바꿔서 계산
        if row < N//2:
            s, e = s-1, e+1
        else:
            s, e = s+1, e-1
    print(ans)