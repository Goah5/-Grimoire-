# Расчёт того сколько "планетарки первого класса" доступных видов нужно
# заправить на заданный объём в "Планету завод по сборке всего второго класса"

offmat = {"Proteins"}  # "Electrolytes"

with open("D:\\Python\Grimoire\\7 заправка планетарки\\2.txt", "r") as f:
    pro = []
    s = list()
    for i in f.readlines():
        if i == "\n":
            continue
        if "#" in i:
            continue
        i = i.split("	")
        if i[0] not in offmat and i[1] not in offmat:
            s += [*i[0:2]]
            # pro.append(i[2])

temp = {}
for i in s:
    try:
        temp[i] += 40
    except:
        temp[i] = 40

su = sum(temp.values())
m3 = (20000-(12529))/0.19  # Можно заменить на
if (inp := input("20000-( ")):
    m3 = (20000-eval(inp.replace(",", ".")))/0.19

tp = []
for i in list(temp.keys()):
    tp.append(f"{i}	{int(temp[i]*m3//su)}")
tp.sort()

prev = int(tp[0][tp[0].index('	')+1:])
for j in tp:
    if (qwe := int(j[j.index('	')+1:])) != prev:
        print()
    print(j)
    prev = qwe

print(f"\nTotal m3: {round(sum([temp[i]*m3//su*0.19 for i in temp]),1)} m3\n")
input("Enter")

print(m3//su, m3/su, su)

# print(pro)
# tp = []
# for i in pro:
#     tp.append(f"{i} {m3//su}")
# tp.sort()
# for j in tp:
#     print(j)
