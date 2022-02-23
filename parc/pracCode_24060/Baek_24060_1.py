import sys

def merge_sort(mylist):
    if len(mylist) <= 1: # 배열크기 1개시 그대로 리턴
        return mylist
    half = len(mylist) // 2
    print('half :', half)                # 중간값
    left_list = merge_sort(mylist[:half])
    print('left_list', left_list)  # 전반부 , 각 런의 가장 왼쪽 데이터 의미
    right_list = merge_sort(mylist[half:])
    print('right_list', right_list)  # 후반부 , 각 런의 가장 쪽 데이터 의미    
    return merge(left_list, right_list)

def merge(left_list, right_list):
    merged_list = []                       # 병합
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] > right_list[0]:
            merged_list.append(right_list[0])  # merged_list 맨 마지막에 추가
            right_list.pop(0)  # right가 left 보다 작으므로 right 요소 끄집어냄
        else:
            merged_list.append(left_list[0])
            left_list.pop(0)

# * while문은 재귀 호출로 merge_sort()를 실행한 후에 left_list나 right_list에 데이터가 남아 있다면, 그 데이터는 이미 정렬된 상태로 남아 있기 떄문에 최종적으로 정렬된 리트에 해당하는 merged_list에 추가함
    if len(left_list) > 0:
        merged_list += left_list
    if len(right_list) > 0:
        merged_list += right_list
    return merged_list


# ! K 번째 저장되는 숫자 출력
# ! 특수조건 : -1 출력
# * N: 배열 A의 크기 / K: 저장횟수 / A: 배열
if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().split()))
    temp_list = A
    print("<정렬전>")
    print(A)
    sorted_data = merge_sort(A)
    print("<정렬후>")
    print(sorted_data)
