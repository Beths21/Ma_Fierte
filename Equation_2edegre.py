####Equation second degre####
import math

a= int (input("entrer a :"))
print (a)
b= int (input("entrer b :"))
print (b)
c= int (input("entrer c :"))
print (c)


###Calcul de delta###
delta = b*b -(4*a*c)

X1 = 0
X2 = 0
X = 0
if delta >0:
    X1 = (-b - math.sqrt(delta)) /(2*a)
    X2 = (-b+math.sqrt(delta))/(2*a)
    print("le resultat est:",X1, X2)
    print("Liste")
    eq=str(a) +"*X^2" + str(b) +"*X" + str(c)
    second_degre = [eq,X1,X2]
    print(second_degre)

    print ("Dictionnaire")
    second_degre = dict()
    second_degre["Equation:"] = str(a) +"*X^2 +" + str(b) +"*X +" + str(c)
    second_degre["Resultat:"] = X1,X2 
    print(second_degre)
elif delta ==0:
    X= -b/(2*a)
    print("le resultat est:",X)
    print("Liste")
    eq=str(a) +"*X^2 +" + str(b)+ "*X +" + str(c)
    second_degre = [eq,X1,X2]
    print(second_degre)

    print ("Dictionnaire")
    second_degre = dict()
    second_degre["Equation:"] = str(a) +"*X^2 +" + str(b) +"*X +" + str(c)
    second_degre["Resultat:"] = X1,X2 
    print(second_degre)

else:
   print("Impossible")   
     



