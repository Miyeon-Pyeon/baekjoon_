T = int(input())

for i in range(T):
  cnt, word = input().split()
  for x in word:
    print(x * int(cnt), end='')
  print()