def bitstring(x):
    return bin(x)[2:]   #vraća bin broj u stringu (bez 0b)
def racunaj(lhs, rhs):
    ost = lhs #ostatak
    div = rhs #djelitelj (12 u primjeru)
    origlen = len(bitstring(div)) #dužina dijelitelja

    count = 1
    while (div | ost) > 2*div:  #pomak za 1 bit lijevo sve dok ne dobijemo
        div <<= 1               #djelitelj koji je veći od ostatka
        count += 1

    rez = 0
    while count > 0:
        rez <<= 1 #pomak rezultata u lijevo za 1 bit
        print(bitstring(rez))
        count -= 1
        print("%14s" % bitstring(ost))  #na početku je to testni broj 1240
        divstr = bitstring(div)         #pretvoren djelitelj u string zbog lakšeg ispisa
        if (ost ^ div) < ost:           #dogodi se da bude ost^div=ost, a to ne prolazi uvjet, pa samo shifta 2 puta
            rez |= 1
            ost ^= div #oduzimanje osta od diva(110000..)

            print(1, " " * (11-len(divstr)), divstr[:origlen]) #samo ispis i pomak djelitelja
        else:
            print(0, " " * (11-len(divstr)), "0" * origlen)
        print(" " * (13-len(divstr)), "-" * origlen) #samo pomicanje crtica za podvlačenje
        div >>= 1 #pomiče djelitelj udesno da može nastavit dijelit,smanjujemo ga nazad
    print("%14s <<< ostatak" % bitstring(ost))
    print(" -> %10s <<< rezultat" % bitstring(rez))

racunaj(0b10011011000, 12)
