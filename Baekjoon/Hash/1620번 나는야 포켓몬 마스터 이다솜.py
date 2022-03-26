"""
1620번 - https://www.acmicpc.net/problem/1620

나는야 포켓몬 마스터 이다솜

reference
1. Dictionary에 값 추가
https://waytods.tistory.com/21

2. Dictionary Get 사용 & key값 존재 여부
https://yunaaaas.tistory.com/46

3. reverse_Dict= dict(map(reversed,Dict.items()))
https://seong6496.tistory.com/72

알게 된 점
1. input = sys.stdin.readline 사용시, input의 끝에 \n이 같이 들어감
2. python3 - 시간초과 / pypy3 - 통과..
"""

# import sys
# input = sys.stdin.readline

N, M = map(int, input().split())
Dict = {}

for i in range(N):
    pokemon = input()
    Dict[i+1] = pokemon
reverse_Dict= dict(map(reversed,Dict.items()))

for _ in range(M):
    test = input()

    ## test가 reverse_Dict의 key 값인 경우 - 이름
    if test in reverse_Dict:
        print(reverse_Dict.get(test))

    ## test가 Dict의 key 값인 경우 - 숫자
    elif int(test) in Dict:
        print(Dict.get(int(test)))