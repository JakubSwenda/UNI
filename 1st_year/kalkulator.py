from math import*
def miejsca():
    a=float(input("Podaj 'a': "))
    b=float(input("Podaj 'b': "))
    c=float(input("Podaj 'c': "))
    d=(b*b)-(4*a*c)
    if d<0:
        print("brak rozwiazan")
    elif d==0:
        x3=(-b)/(2*a)
        print("jest jedno miejsce zerowe: ",x3)
    elif d>0:
        x1=((-b)-(sqrt(d)))/(2*a)
        x2=(b-(sqrt(d)))/(2*a)
        print("Delta wynosi: ", d)
        print("Miejsce zerowe x[1]: ", x1)
        print("Miejsce zerowe x[2]: ", x2)
    
def kalkulator(): 
    z=int(input("Wybierz dzialanie: 1-dodawanie, 2-odejmowanie, 3-mnozenie, 4-dzielenie, 5-liczenie miejsca zerowego "))
    if z==1:
        x=float(input("Podaj pierwsza liczbe: "))
        y=float(input("Podaj druga liczbe: "))
        print("Wynik dodawania to: ", x+y)
    elif z==2:
        x=float(input("Podaj pierwsza liczbe: "))
        y=float(input("Podaj druga liczbe: "))
        print("Wynik odejmowania to: ", x-y)
    elif z==3:
        x=float(input("Podaj pierwsza liczbe: "))
        y=float(input("Podaj druga liczbe: "))
        print("Wynik mnozenia to: ", x*y)
    elif z==4 and y!=0:
        x=float(input("Podaj pierwsza liczbe: "))
        y=float(input("Podaj druga liczbe: "))
        print("Wynik dzielenia to: ", x/y)
    elif z==5:
        miejsca()
    if z==4 and y==0:
        print("Nie mozna dzielic przez 0!")
    
    k=int(input("Czy chcesz kontynuowac? TAK-wcisnij '1'  NIE-wcisnij 2  "))
    if k==1:
        kalkulator()
    else:
        print("Do widzenia")
kalkulator()
