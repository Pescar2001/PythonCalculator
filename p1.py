
import math

while True:
    print ("\n Alege metoda.\n \n0-Adunare\n1- Scadere\n2- Inmultire\n3-Impartire\n4-Exponentiere " )
    oper= input("\nOptinea ta ")
 #adunare
    if oper=="0":
        v1= float(input("\nPrinma valoare:"))
        v2= float(input("\nA doua valoare:"))
        suma= v1 + v2
        print("\nRezultatul este: " + str(suma))  
        inapoi = input("\Mergi inapoi y\n")
        if inapoi=="y":
            continue
        else:
            break
  #scadere 
    if oper =="1":
        v1=float(input("\nPrima valoare:"))
        v2= float(input("\nA doua valoare:"))
        diferenta= v1-v2
        print("\nRezultatul este: "+ str(diferenta) )
        inapoi = input("\nMergi inapoi y\n")
        if inapoi== "y":
            continue
        else:
            break
#Inmultire
    if oper=="2":
        v1=float(input("\nPrima valoare:"))
        v2= float(input("\nA doua valoare:"))
        produs=v1 * v2
        print("\nRezultatuleste: " + str(produs))
        inapoi= input("\nMergi inapoi y\n")
        if inapoi== "y":
            continue
        else:
            break
 #impartire
    if oper=="3":
        v1=float(input("\nPrima valoare:"))
        v2=float(input("\nA doua valoare:"))
        rest= v1 / v2
        print("\nRezultatul este: "+ str(rest))
        inapoi = input("\nMergi inapoi y\n")
        if inapoi =="y":
            continue
        else:
            break
  #Exponentiere
    if oper=="4":
        v1=float(input("\nPrima valoare:"))
        v2=float(input("\nA doua valaore:"))
        ridicare = v1 ** v2
        print("\nRezultatul este: " + str(ridicare))
        inapoi= input ("\nMergi inapoi y\n" )
        if inapoi == "y":
            continue
        else:
            break