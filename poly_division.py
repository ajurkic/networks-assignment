from itertools import zip_longest
 
def stupanj(polinom):
    while polinom and polinom[-1] == 0:
        polinom.pop()
    return len(polinom)-1
 
def dijeljenje(N, D):
    stManjeg = stupanj(D)
    stVeceg = stupanj(N)
    if stManjeg < 0: raise ZeroDivisionError

    if stVeceg >= stManjeg:
        rez = [0] * stVeceg #reset rez, postavi mu dužinu na stupanj N
        while stVeceg >= stManjeg:
            #pomocna varijabla d
            d = [0]*(stVeceg - stManjeg) + D                                   #pomak udesno do najvećeg stupnja da bi mogli oduzimat
            mult = rez[stVeceg - stManjeg] = N[-1] / float(d[-1])              #dijeljenje,spremanje u rez
            d = [koef*mult for koef in d]                                      #pomnozi svaki element s rez gornjeg dijeljenja
            N = [koefN - koefd for koefN, koefd in zip_longest(N,d)]           #promjena predznaka, oduzimanje
            stVeceg = stupanj(N)                                               #azuriranje trenutnog najveceg stupnja
        ostatak = N

    else:
        rez = [0]
        ostatak = N
    return rez, ostatak

print("Dijeljenje polinoma: ")
N = [-42, 0, -12, 1]
D = [-3, 1, 0, 0]
print("  %s / %s =" % (N,D))
print(" %s i ostatak %s" % dijeljenje(N, D))