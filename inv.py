basicinv = {
    "money" : 0,
    "weapon" : "",
    "stone" : 0
}

def getmoney(moneyy):
    basicinv["money"] += moneyy

def usemoney(moneyy):
    basicinv["money"] -= moneyy

def changeweapon(newweapon):
    basicinv["weapon"] = newweapon

def getstone(stones):
    basicinv["stone"] += stones

def usestone(stones):
    basicinv["stone"] -= stones

inv = [""]
for i in range(9):
    inv.append("")




