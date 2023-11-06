n = int(input())
scores = [0]  #계단의 점수를 저장할 리스트
for _ in range(n):
    scores.append(int(input()))

#dp[i]는 i번째 계단까지 도달했을 때 얻을 수 있는 최대 점수
dp = [0] * (n + 1)

#첫 번째 계단의 점수는 그대로 저장
dp[1] = scores[1]

#두 번째 계단까지의 최대 점수는 첫 번째와 두 번째 계단의 점수 합
if n > 1:
    dp[2] = scores[1] + scores[2]

for i in range(3, n + 1):
    # i번째 계단을 오를 때, 바로 이전 계단(i-1)을 밟고 왔을 경우와
    # 한 계단 건너뛰어 온 경우(i-2) 중 최대 점수를 선택하여 더함
    dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

# 마지막 도착 계단은 무조건 밟아야 하므로 dp[n]
print(dp[n])