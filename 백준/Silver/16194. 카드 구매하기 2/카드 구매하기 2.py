N = int(input())
P = [0] + list(map(int, input().split()))  # 카드 팩 가격, 0번 인덱스를 사용하지 않음
dp = [0] + [float('inf')] * N  # 최소 가격을 저장할 DP 테이블, 초기값은 무한대로 설정

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + P[j])

print(dp[N])
