from icecream import ic # "Информативный" print



def inputMatpool() -> dict[str, int]:
    matpool = dict()
    while temp := input():
        t = [temp[:temp.index("*")],temp[temp.index("*")+1:]]
        # t[0] = t[0].lower()
        try:
            matpool[t[0]] += int(t[1])
        except:
            matpool[t[0]] = int(t[1])
    return matpool


def simCraft(matpool, recipes) -> tuple[dict]:
    usedmat = dict()
    for r in recipes:
        ic(r)
        for i in r:
            ic(i)
            try:
                if matpool[i] < 10:
                    break
            except:
                break
        else:
            ic(r)
            for i in r:
                ic(i, r)
                matpool[i] -= 10
                try:
                    usedmat[i] += 10
                except:
                    usedmat[i] = 10

    return matpool, usedmat


def getRecipesList() -> list[list[str]]:

    with open("D:\\Python\\Grimoire\\7 заправка планетарки\\3.txt", "r") as f:
        RecipeList = list()
        for i in f.readlines():
            if i == "\n":
                continue    
            if "#" in i:
                continue
            temp = i.split("	")[0:3]
            if temp[2] == "-":
                RecipeList.append(temp[0:2])
            else:
                RecipeList.append(temp)

    return RecipeList


def main():
    matpool = inputMatpool()
    recipes = getRecipesList()

    usedmat = dict()
    oldMatpool = {}
    while matpool != oldMatpool:
        oldMatpool = matpool.copy()
        matpool, temp = simCraft(matpool, recipes)
        for i in temp:
            try:
                usedmat[i] += temp[i]
            except:
                usedmat[i] = temp[i]


    # ic.enable()
    ic(recipes)
    ic(usedmat)
    ic(matpool)

    print()
    pri = []
    su = 0
    for i, j in usedmat.items():
        pri.append(f"{i}*  {j}")
        su += j
    pri.sort()

    prev = 0
    for i in sorted(pri):
        if prev == int(i.split('  ')[-1]):
            print("  ", end="")
        prev = int(i.split('  ')[-1])
        print(i)
    print(f"\nTotal m3: {su*0.75} m3\n")
    input("Enter")

ic.disable()
main()
