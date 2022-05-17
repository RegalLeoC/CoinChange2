import json


# Recursive Coin Change problem

def CoinChange(coins, money, changeamount):
    missing = 0

    for i in range(len(changeamount)):
        missing = changeamount[i] + missing

    missing = missing - money
    if missing == 0:
        return True

    for i in range(len(coins)):
        if (coins[i] + missing) <= 0:
            missing = coins[i] + missing
            newchangeamount = changeamount
            newchangeamount.append(coins[i])
            if CoinChange(coins, money, newchangeamount):
                return True


def recCoin(coins, money):
    changeamount = [0]
    change = (CoinChange(coins, money, changeamount))
    return changeamount


# User Input
coins = [10,5, 2, 1]
cost = int(input("Inserte el precio de su compra: "))

while cost > 0:
    print(f"Monto a pagar: {cost}")
    money = int(input("Inserte su dinero: "))
    cost = cost - money

if cost < 0:
    changeneeded = -1 * (cost)
    print(f"Se le devolvera {changeneeded} de cambio.")

if cost == 0:
    print("Cambio exacto.")

print(recCoin(coins, changeneeded)[1:])
