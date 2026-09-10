n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

# Please write your code here.
hm = {}
re_hm = {}
for key, value in enumerate(words):
    hm[str(key)] = value
    re_hm[str(value)] = key

for i in range(m):
    key = queries[i]

    a = hm.get(key)
    b = re_hm.get(key)
    if a is not None:
        print(a)
    if b is not None:
        print(b)