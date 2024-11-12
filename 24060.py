def merge_sort(A, p, r): # A[p ~ r]을 오름차순 정렬한다.
  if p < r:
    q = (p + r) // 2; # q는 p, r의 중간 지점
    merge_sort(A, p, q)       # 절반에서 왼쪽 부분 정렬 (정렬은 이 재귀된 merge_sort 내의 merge()에서 이루어짐). 이 한 줄이 결국 return하는 건 완전히 다 정렬된 왼쪽 부분
    merge_sort(A, q + 1, r)   # 절반에서 오른쪽 부분 정렬 (정렬은 이 재귀된 merge_sort 내의 merge()에서 이루어짐). 이 한 줄이 결국 return하는 건 완전히 다 정렬된 오른쪽 부분
    merge(A, p, q, r)         # 왼쪽 부분과 오른쪽 부분 병합

# A[p~q]와 A[(q+1)~r]을 병합하여 A[p~r]을 오름차순 정렬된 상태로 만든다.
# A[p~q]와 A[(q+1)~r]은 이미 오름차순으로 정렬되어 있다.
def merge(A, p, q, r):
  # p는 시작, q는 절반, r은 끝
  global cnt, res
  i = p # i는 p부터 시작 위치
  j = q + 1 # j는 q+1부터 시작 위치
  tmp = []
  
  while i <= q and j <= r:
    if A[i] <= A[j]: # 왼쪽 배열의 값이 더 작은 경우
      tmp.append(A[i]) # tmp에 더 작은 값 추가
      i += 1
    else:
      tmp.append(A[j]) # 오른쪽 배열의 값이 더 작은 경우
      j += 1 # tmp에 더 작은 값 추가
    
  while i <= q: # 왼쪽 배열 부분이 남은 경우.
    tmp.append(A[i]) # 남은 부분을 tmp에 추가
    i += 1
  
  while j <= r: # 오른쪽 배열 부분이 남은 경우
    tmp.append(A[j]) # 남은 부분을 tmp에 추가
    j += 1
  
  i = p
  t = 0
  
  while i <= r:  # 결과(tmp)를 A에 저장. 현재 r 값에 따라 A의 일부만 변경.
    A[i] = tmp[t]
    cnt += 1 # cnt는 global이라 재귀됨에 따라 초기화되지 않고 누적됨.
    if cnt == K: # A에 하나하나 반영되는 과정에서, 전체로 봤을 때 K번째로 A에 반영하는 값을 출력
       res = A[i]
       break
    i += 1
    t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(A, 0, N - 1)
print(res)