def input_EveTable():
    while (ta := input()) != "":
        yield ta.split("	")

c = 0
for i in (list(input_EveTable())):
    t = i[4]
    c += (int("".join([j for j in t[:t.index(",")] if j.isdigit()])))

print(c-(c*0.036))