# 1이 될 때까지
# 하
# 그리드
## 2번째 답안 ( 어려운디 💦💦)

# N, K를 공백으로 구분하여 입력받기
N, K = map(int, input().split()) ##* 18, 3
result = 0

while True:
    # (N == K로 나누어떨어지는 수) 가 될 때까지 1씩 빼기
    target = (N // K) * K   ##* (18//3) * 3 -> 4*3 =12      ##* (4 // 3) * 3 =1
    result += (N - target)  ##* result + (18 - 12)          ##* (4-1) = 3
    N = target              ##* 12                          ##* 1
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if N < K:
        break
    # K로 나누기
    result += 1             ##* 6+1
    N //= K                 ##* 12//3 = 4

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (N - 1)                                           ##* 3 +(1-1) = 3
print(result)