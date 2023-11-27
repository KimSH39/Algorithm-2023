x, y = map(int, input().split())
sum_val = x + y
big = max(x, y)
a = 0
is_possible = True

#가능한 'a' 값을 찾기
for i in range(big + 1):
    if (sum_val * 2) - i == i ** 2:
        a = i
        is_possible = True
        break
    elif (sum_val * 2) - i < i ** 2:
        is_possible = False
        break
    else:
        is_possible = False

#가능한 경우
if is_possible:
    cnt = 0
    
    # 최소 이길 횟수 계산
    for i in range(a, 0, -1):
        if x >= i:
            x -= i
            cnt += 1
    
#결과 출력
    print(cnt)
else:
#불가능한 경우
    print(-1)
