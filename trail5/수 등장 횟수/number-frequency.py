n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# Please write your code here.
hashmap = {}
for i in range(n):
    hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1

for k in nums:
    answer = hashmap.get(k, 0)
    print(answer, end = ' ')