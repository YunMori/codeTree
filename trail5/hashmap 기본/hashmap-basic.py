n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
hashmap = {}
for i in range(n):
    if commands[i][0] == 'add':
        k, v = commands[i][1], commands[i][2]
        hashmap[k] = v
    elif commands[i][0] == 'remove':
        k = commands[i][1]
        del hashmap[k]
    elif commands[i][0] == 'find':
        k = commands[i][1]
        v = hashmap.get(k)
        print(v)
