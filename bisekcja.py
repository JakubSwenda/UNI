a=int(input("Podaj poczatek przedzialu: "))
b=int(input("Podaj koniec przedzialu: "))

l=float(input("Podaj epsilon: "))#najlepiej dac 0.001, wtedy jest dosc dokladnie

def funkcja1(x):
    return 2*(x*x)-(2*x)-1
def bisekcja(a,b,l):
    if funkcja1(a)*funkcja1(b)>0:
        print("Nieprawidlowy przedzial!")
        return
   
    while abs(a-b)>l:
        c=(a+b)/2
        if funkcja1(c)==0:
            print("To jest miejsce zerowe: ", c)
       
        else:
            if funkcja1(a)*funkcja1(c)>0:
                a=c
            else:
                b=c
    print("To jest miejsce zerowe: ", c)



bisekcja(a, b, l)
