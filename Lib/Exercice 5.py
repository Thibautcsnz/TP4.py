m=0
j=0
n=0
a=0
n=(input("Donnez la date dans le format JJMMAAAA :"))

if len(n)==8:
    j = int(n[0] + n[1])
    m = int(n[2] + n[3])
    a = int(n[4] + n[5] + n[6] + n[7])

    if 0<a and a<9999:
        if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
            if 1 <= j and j <= 31:
                print("Date Correcte")
            else:
                print("Date Incorrecte")
        elif m==2:
                if (a%4==0) and (a%100!=0) or (a%400==0):
                    if 1<=j and j <= 29:
                        print("Date correcte")
                    else:
                        print("Date Incorrecte")
                else:
                    if 1<=j and j<=28:
                        print("Date correcte")
                    else:
                        print("Date Incorrecte")
        elif m==4 or m==6 or m==8 or m==9 or m==11:
                if 1<=j and j<=30:
                        print("Date correcte")
                else:
                    print("Date Incorrecte")
        else:
            print("Date Incorrecte")
    else:
        print("Date Incorrecte")
else:
    print("Date Incorrecte")







