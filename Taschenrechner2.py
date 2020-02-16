print("Möchtest du Addieren(Tippe 1), Subtrahieren(Tippe 2), Multiplizieren (Tippe 3) oder Dividieren(Tippe 4)?")
Eingabe=int(input())
if Eingabe==1:
    print("Gebe eine Zahl ein")
    Zahl1=float(input())
    print("Gebe noch eine Zahl ein")
    Zahl2=float(input())
    Ergebnis=Zahl1+Zahl2
    print("Ergebnis=", Ergebnis);
if Eingabe==2:
    print("Gebe eine Zahl ein")
    Zahl1=float(input())
    print("Gebe noch eine Zahl ein")
    Zahl2=float(input())
    Ergebnis=Zahl1-Zahl2
    print("Ergebnis=", Ergebnis);
if Eingabe==3:
    print("Gebe eine Zahl ein")
    Zahl1=float(input())
    print("Gebe noch eine Zahl ein")
    Zahl2=float(input())
    Ergebnis=Zahl1*Zahl2
    print("Ergebnis=",Ergebnis);
if Eingabe==4:
    print("Gebe eine Zahl ein")
    Zahl1=float(input())
    print("Gebe noch eine Zahl ein")
    Zahl2=float(input())
    if Zahl2==0:
        print("Tut mir leid, das geht leider nicht:(")
    else:
        Ergebnis=Zahl1/Zahl2
        print("Ergebnis=",Ergebnis)

