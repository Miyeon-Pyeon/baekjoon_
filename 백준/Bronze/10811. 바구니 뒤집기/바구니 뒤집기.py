N, M = map(int, input().split())

arr = [i for i in range(1, N+1)]

for i in range(M):
  j, k = map(int, input().split())
  temp = arr[j-1:k]
  temp.reverse()
  arr[j-1:k] = temp

for i in range(N):
  print(arr[i], end= ' ')