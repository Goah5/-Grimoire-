from icecream import ic


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

    with open("3.txt", "r") as f:
        RecipeList = list()
        for i in f.readlines():
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
    for i, j in usedmat.items():
        pri.append(f"{i}*	{j}")
    for i in sorted(pri):
        print(i)


ic.disable()
main()
