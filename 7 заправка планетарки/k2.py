#Расчёт того сколько "планетарки первого класса" доступных видов нужно 
# заправить на заданный объём в "Планету завод по сборке всего второго класса"

offmat = {"Proteins",
          "Electrolytes"}

with open("2.txt", "r") as f:
    s = list()
    for i in f.readlines():
        i = i.split("	")
        if i[0] not in offmat and i[1] not in offmat:

            s += [*i[0:2]]

temp = {}
for i in s:
    try:
        temp[i] += 40
    except:
        temp[i] = 40

su = sum(temp.values())
m3 = (10000)/0.19 # Можно заменить на m3 = float(input())/0.19

tp = []
for i in list(temp.keys()):
    tp.append(f"{i} {int(temp[i]*m3//su)}")
tp.sort()
for j in tp:
    print(j)

input("Enter")

print(m3//su, m3/su, su)
