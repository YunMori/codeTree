n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
hashmap = {}
for word in words:
    hashmap[word] = hashmap.get(word, 0) + 1
answer = 0
for mx in hashmap.values():
    answer = max(answer, mx)
print(answer)