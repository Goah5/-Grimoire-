sl = []
inp = "_"
while (inp := input()) != "":
    sl.append(str(inp.split()[1::]))
t = {}
for i in sl:
    try:
        t[i] += 1
    except:
        t[i] = 1
print(t)
#