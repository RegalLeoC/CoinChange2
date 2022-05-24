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
# board = [['_' for j in range(8)] for i in range(8)]
# coinlist = [[0 for i in range(len(coinsname))] for j in range(len(coinsamount))]
#
# coinlist = [[0 for i in range(len(coinsname))] for j in range(len(coinsamount))]

# for i in range(len(coinsname)):
#     for j in range(len(coinsamount)):
#         coinlist[i][j] = [coinsname[i],coinsamount[j]]



# j = 0
# i = 0
# while j < len(coinsamount) and i < len(coinsname):
#     coinlist[i][j] = [coinsname[i], coinsamount[j]]
#     i = i + 1
#     j = j + 1

coinlist = []

j = 0
i = 0
while j < len(coinsamount) and i < len(coinsname):
    coinlist.append([coinsname[i], coinsamount[j]])
    i = i + 1
    j = j + 1



print(coinlist)

#Print coso
print(five)
print(five.keys())
print(five.values())

# [1[2], 2[23], 5[38]]