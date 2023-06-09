"""
백준 1309 - 동물원
NxN 동물원이 있다. 사자를 가로로 세로로 붙어 있지 않게 배치
2*N배열에 사자를 배치하는 경우의 수를 출력
사자를 한 마리도 배치하지 않는 경우도 하나의 경우의 수로 친다고 가정
첫째줄 N 입력
사자를 배치하는 경우의 수를 9901로 나눈 나머지 출력
"""

# 수학적 공식을 세워보자! 규칙을 생각하면 될 것 같음
# dp[0] = 1 , dp[1] = 3 , dp[2] = 7 ,dp[3] = 17, dp[4] = 41
# dp[1] = 2 * dp[i-1] + dp[i-2] ? -> 아님
# 조건이 더 있었음!
# 앞에 존재하는 경우의 수에 타일을 한줄씩 추가해야됨
# 이 추가 조건은 3개로 추가하기전 마지막 타일이 -> 1. 다 비어있는 경우 2. 왼쪽에 배치 3. 오른쪽에 배치 이 3개에 따라 나눠서 분류
n = int(input())
# 모든 배열에 같은 숫자 추가? 를 위해서 일부로 이케 함
dp = [0]*(n+1)
for i in range(n+1) :
    dp[i] = [0,0,0]
# 다 비어있는 경우
dp[1][0] = 1
# 왼쪽에 배치
dp[1][1] = 1
# 오른쪽에 배치
dp[1][2] = 1

# 9901을 나누라는 이유가 수가 커서이니까 미리 나눠서 계산해야됨
for i in range(2, n + 1):
    dp[i][0] =(dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) %9901
    dp[i][1] =(dp[i - 1][0] + dp[i - 1][2]) % 9901
    dp[i][2] =(dp[i - 1][0] + dp[i - 1][1]) % 9901

print(sum(dp[n]) % 9901)