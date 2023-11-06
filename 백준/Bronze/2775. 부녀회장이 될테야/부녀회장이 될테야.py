# 아파트 생성
dp_apt = [[0] * 15 for _ in range(15)]

for i in range(15):
    dp_apt[0][i] = i  # 0층의 i호는 i명 입주 가능
    dp_apt[i][1] = 1  # i층의 1호는 1명 입주 가능

for i in range(1, 15):
    for j in range(2, 15):
        dp_apt[i][j] = dp_apt[i][j - 1] + dp_apt[i - 1][j]

t = int(input())  # 테스트 케이스 수
result = []

for _ in range(t):
    k = int(input())  # 층 수
    n = int(input())  # 호 수
    result.append(dp_apt[k][n])

for res in result:
    print(res)
