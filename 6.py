#Симуляция лопата
m3 = 0
while temp := input():
    temp = temp.split("	")[2]
    m3 += int(temp.replace("\xa0","")[:-3])

mine = [[20, 24.5], [400*1.33, 90.5]]  # [[m3, sek]]

t = 0
while m3 > 0:
    t += 1
    for i, sek in mine:
        if t % sek == 0:
            m3 -= i

# print(t, m3)
print(f"{t//60//60}h {t//60}m {t-t//60*60}s")



