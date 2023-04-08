# 숫자 카드 게임
# 하
# 그리드
## 2중 반복문 구조를 이용하는 답안

N, M = map(int, input().split())

result = 0
# 한 줄 씩 입력받아 확인
for i in range(N):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력