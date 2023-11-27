import sys
input = sys.stdin.readline  # 한 줄에 여러 입력 값 받기 위한 함수

s = list(input().rstrip())  # 오른쪽 공백 삭제 후 입력 값을 리스트로 변환
t = list(input().rstrip())

switch = False  # 스위치 변수 초기화
while t:
    if t[-1] == 'A':  # t 리스트의 마지막 요소가 'A'인 경우 마지막 요소 제거
        t.pop()
    elif t[-1] == 'B': 
        t.pop() 
        t.reverse()  # 리스트 뒤집기
    if s == t:  # s 리스트와 t 리스트가 같은 경우
        switch = True  # 스위치 변수를 True로 변경
        break 
        
if switch:  # 스위치 변수가 True인 경우
    print(1)  
else:
    print(0) 
