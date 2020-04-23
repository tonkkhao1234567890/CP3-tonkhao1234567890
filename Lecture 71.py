menulist = []
pricelist = []
while True:
    Menulist = input("Menu : ")
    if Menulist == "exit":
        break
    else:
        Pricelist  = float(input("Price : "))
        menulist.append(Menulist)
        pricelist.append(Pricelist)
def Showbill():
    print("=====Food=====")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])
    print("Total--------------")
    print(str(sum(pricelist)))
Showbill()

