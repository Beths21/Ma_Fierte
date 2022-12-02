from random import randrange



jwe = 1
while jwe == 1:
    chans = 5
    nonb_odinate = randrange(0,500) 
    while chans > 0:
        print("rete ", chans, " chans")
        print("ou dwe chwazi ant 0 a 500")
        vale_chwazi = int(input("ki nomb ou chwazi? "))

        if vale_chwazi < nonb_odinate:
            print("vale a tro piti!") 
        if vale_chwazi > nonb_odinate:
            print("vale a tro gran!")
        if vale_chwazi == nonb_odinate:
            print("ou genyen!") 
            break

        chans -= 1
    if chans == 0:
        print("ou pedi!")
        print(f"vale a se: {nonb_odinate}")
        jwe = int(input("siw vle kontinye jwe , peze 1: "))


