'''
16진수 1자리는 2진수 4자리로 표시된다.
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
<단, 2진수의 앞자리 0도 반드시 출력한다.>
예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.
0100011111111110
[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 자리 수 N과 N자리 16진수가 주어진다. 1<=N<=100
16진수 A부터 F는 대문자로 표시된다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
[아이디어]
1. int(a, b) 일때 첫번째 인자가 2, 8, 16진수로 바뀔 수 있는 문자열이고 b에 진수를 쓰면 해당 숫자가 10진수로 바뀝니다
2. ''.format()를 이용하면 숫자를 다른 진법의 수로 바꿀 수 있어요
'''
import sys
sys.stdin = open("5185.txt","r")

for tc in range(int(input())):
    print('#{} {}'.format(tc+1, ''.join(['{:04b}'.format(int(s,16)) for s in input().split()[1]])))