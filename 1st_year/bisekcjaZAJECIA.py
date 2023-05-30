def wybor():
    print("Wybierz co chcesz policzyc")
    w=int(input("1->Miejsce zerowe funkcji:2x^2-2x-1  2->Miejsce zerowe funkcji:4x^2+3x-5  3->Miejsce zerowe funkcji:5x^2+6x-3  ABY WYJSC WCISNIJ 0   Twoj wybor->"))
    if w==0:
        return
    if w==1: #przedzial ktory dziala (1,4)
        p=int(input("Podaj poczatek przedzialu:  "))
        k=int(input("Podaj koniec przedzialu:  "))    
        l=0.001
        a=2
        b=-2
        c=-1
        def fkwad1(x):
            return a*(x*x)+(b*x)+c
        def bisekcja(p,k,l):
            if fkwad1(p)*fkwad1(k)>0:
                print("Nieprawidlowy przedzial!!")
                return

            while abs(p-k)>l:
                d=(p+k)/2
                if fkwad1(d)==0:
                    print("To jest miejsce zerowe: ", d)
                else:
                    if fkwad1(p)*fkwad1(d)>0:
                        p=d
                    else:
                        k=d
            print("To jest miejsce zerowe: ",d)
            return
        bisekcja(p,k,l)
    if w==2: #przedzial ktory dziala (0,4)
        p=int(input("Podaj poczatek przedzialu:  "))
        k=int(input("Podaj koniec przedzialu:  "))    
        l=0.001
        a=4
        b=3
        c=-5
        def fkwad2(x):
            return a*(x*x)+(b*x)+c
        def bisekcja(p,k,l):
            if fkwad2(p)*fkwad2(k)>0:
                print("Nieprawidlowy przedzial!!")
                return

            while abs(p-k)>l:
                d=(p+k)/2
                if fkwad2(d)==0:
                    print("To jest miejsce zerowe: ", d)
                else:
                    if fkwad2(p)*fkwad2(d)>0:
                        p=d
                    else:
                        k=d
            print("To jest miejsce zerowe: ",d)
            return
        bisekcja(p,k,l)
    if w==3: #przedzial ktory dziala (0,2)
        p=int(input("Podaj poczatek przedzialu:  "))
        k=int(input("Podaj koniec przedzialu:  "))    
        l=0.001
        a=5
        b=6
        c=-3
        def fkwad3(x):
            return a*(x*x)+(b*x)+c
        def bisekcja(p,k,l):
            if fkwad3(p)*fkwad3(k)>0:
                print("Nieprawidlowy przedzial!!")
                return

            while abs(p-k)>l:
                d=(p+k)/2
                if fkwad3(d)==0:
                    print("To jest miejsce zerowe: ", d)
                else:
                    if fkwad3(p)*fkwad3(d)>0:
                        p=d
                    else:
                        k=d
            print("To jest miejsce zerowe: ",d)
            return
        bisekcja(p,k,l)
    
wybor()