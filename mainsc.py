import inv
import player as pl
import status as st
import colorama as col

p = pl.player()
skills = p.skills
lev = p.lev
hp = p.hp
mxhp = p.mxhp
mp = p.mp
mel = p.mel
dmg = p.dmg
spd = p. spd
job = p.job
w = inv.basicinv["weapon"]
realtitle = "dd"#p.realtitle
money = inv.basicinv["money"]
inve = inv.inv

def plinform(name):
    print(col.Fore.GREEN , "플레이어",col.Fore.WHITE,"로 참가하셨습니다",col.Back.RESET)
    print()
    print("name:",name,"       level:",lev)
    print("money:",money,"       title:",col.Fore.LIGHTRED_EX,realtitle,col.Fore.RESET)
    print("hp:",hp,"/",mxhp,"       mp:",mp)
    print("dmg:",dmg,"       spd:",spd)
    print("근접:",mel,"       job:",job)
    print("skill1:",skills[0],"  skill2:",skills[1],"  skill3:",skills[2])
    print("weapon:",w)

def inventory():
    print(col.Fore.GREEN , "플레이어",col.Fore.WHITE,"로 참가하셨습니다",col.Back.RESET)
    print()
    print("money:",money,"       weapon:",w)
    print(inve[0],",",inve[1],",",inve[2],",",inve[3],",",inve[4],",",inve[5],",",inve[6],",",inve[7],",",inve[8],",",inve[9])
    z = 1
    while z == 1:
        x = input("[y/n]인벤토리에서 버리고싶은 물건이 있습니까?")
        if x == "y":
            y = int(input("물건의 번호를 입력해주십시오"))
            if y <= 10:
                inve[y-1] = ""
                print(col.Fore.BLUE,"승인되었습니다.",col.Fore.RESET)
                z = 0
        elif x == 'n':
            z = 0
        else:
            print(col.Fore.RED,"Error")
            print("다시 입력해 주십시오",col.Fore.RESET)

    #def

plinform("dd")
print()
inventory()