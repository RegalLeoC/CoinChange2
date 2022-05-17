import json

with open("coin-change.json") as save:
    coinsave = json.load(save)
    save.close()


five = coinsave

# Lista de valores
coinsname = []

for i in five.keys():
    coinsname.append(int(i))
print(coinsname)

#Lista de cantidades
coinsamount = []

for i in five.values():
    coinsamount.append(int(i))
print(coinsamount)

#Newlist
coinlist = [for i in range(len(coinsname)) for j in range(len(coinsamount))]

for i in range(len(coinsname)):
    for j in range(len(coinsamount)):
        coinlist[i][j] = [coinsname[i]][coinsamount[j]]

print(coinlist)

#Print coso
print(five)
print(five.keys())
print(five.values())