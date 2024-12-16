arr = []

for i in range(10):
  A = int(input())
  if A % 42 not in arr:
    arr.append(A % 42)
print(len(arr))