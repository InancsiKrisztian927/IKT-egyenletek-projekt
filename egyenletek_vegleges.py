import math

def menu():
    print("[1]Elsőfokú egyenlet")
    print("[2]Másodfokú egyenlet")
    print("[0]Kilépés")

menu()
option = int(input("Válassz a lehetőségek közül: "))

while(option != -1):
    if (option == 1):
        print("\tElsőfokú egyenlet: a*x+b=c")

        a = int(input("\tKérem az a együtthatót: "))
        b = int(input("\tKérem a b együtthatót: "))
        c = int(input("\tKérem a c együtthatót: "))

        if (a!=0):
            x1=(c-b)/a
            print("\t\t"+str(x1))

        elif(a==0 and b==0):
            print("\t\tMinden x megoldás.")
            

        elif(a==0 and b!=0):
            print("\t\tNincs megoldás!")
            

        else:
            print("\t\tNincs megoldás!")

            

    elif (option == 2):
        print("\tMásodfokú egyenlet" )

        a = int(input("\tKérem az a együtthatót: "))
        b = int(input("\tKérem a b együtthatót: "))
        c = int(input("\tKérem a c együtthatót: "))

        s = b*b - 4*a*c
        if (s < 0):
            txt = "\t\tNincs megoldás."
            print(txt)
        else:   
            x1 = (-1*b  + math.sqrt(s))/2 * a
            x2 = (-1*b  - math.sqrt(s))/2 * a

            txt = "\t\tMegoldás: " + str(x1)+ "\t"+str(x2)
            print(txt)
            
    elif (option == 0):
        quit()
        
    else:
        print("Érvénytelen lehetőség.")

    print()
    menu()
    option = int(input("Válassz a lehetőségek közül: "))
