"""
3613번 - https://www.acmicpc.net/problem/3613

Java vs C++

reference
1. string 한글자씩 끊어서 리스트로
https://ghdwn0217.tistory.com/58

2. 알파벳 아스키코드
https://www.naragara.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-python-%EC%95%84%EC%8A%A4%ED%82%A4%EC%BD%94%EB%93%9Cascii-%EB%B3%80%ED%99%98-%EB%B0%A9%EB%B2%95ord-chr-hex-%EB%B0%8F-%EC%95%84%EC%8A%A4%ED%82%A4%EC%BD%94/

3. 문자열 특정 문자 제거
https://latte-is-horse.tistory.com/200
"""

import sys
input = sys.stdin.readline

def is_cpp(alphabets):
    count = -2
    for i in range(len(alphabets)):
        if alphabets[i] == "_":
            if count == i - 1:  return False
            else:               count = i
        elif 65 <= ord(alphabets[i]) <= 90: return False
    return True

def isJava(alphabets):
    if 65 <= ord(alphabets[0]) <= 90: return False
    return True

def cpp_to_java(alphabets):
    count = 0
    for alphabet in alphabets:
        if alphabet == "_":
            count += 1
        else:
            if count == 1:
                count = 0
                print(chr(ord(alphabet)-32),end="")
            else:
                print(alphabet, end="")
    print()

def javaToCpp(alphabets):
    for alphabet in alphabets:
        if 65 <= ord(alphabet) <= 90:
            print(f"_{chr(ord(alphabet)+32)}",end="")
        else:
            print(alphabet, end='')
    print()

variable = input().rstrip()
java, cpp, nothing = False, False, True
alphabets = list(variable)

## cpp 문법에 맞는지 확인하기 위한 과정
if "_" in alphabets and alphabets[0] != "_" and alphabets[-1] != "_":
    if is_cpp(alphabets):
        cpp, nothing = True, False

## java 문법에 맞는지 확인하기 위한 과정
elif "_" not in alphabets:
    if isJava(alphabets):
        java, nothing = True, False

if nothing: print("Error!")
elif cpp:   cpp_to_java(alphabets)
elif java:  javaToCpp(alphabets)