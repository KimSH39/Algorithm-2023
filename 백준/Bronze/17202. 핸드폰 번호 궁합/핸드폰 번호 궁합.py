x = list(input())
y = list(input())
temp=[]
answer = ''

# 두 문자열을 하나씩 합쳐서 answer에 저장
for i in range(8):
    answer += x[i] + y[i]
#answer의 길이가 2가 되기 전까지 반복하고 두 합의 일의 자리 수만 temp에 append
while len(answer) != 2:
    for i in range(len(answer) - 1):
        temp.append(str((int(answer[i]) + int(answer[i + 1])) % 10))
    answer = ''.join(temp)
    temp=[]
print (answer)