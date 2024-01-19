from IR import IR
from Employe import Employe
from Formateur import Formateur
import datetime
from Agent import Agent
f1 = Formateur("soukayna",datetime.date(2005,10,20),datetime.date(2024,3,5),6000,4)
print(f1.__str__())
a1 = Agent("sanae",datetime.date(2004,1,2),datetime.date(2024,7,9),5000,2000)
employes = [f1, a1]
print("_______menu_______:")
print("1  Afficher les employes")
print("2  Ajouter")
print("3  Supprimer")
print("4 Modifie")
print("5 Quitter")
a = int(input("veuillez entrer votre choix : "))
if a == 1 :
    for i in employes :
        print(i.__str__())
elif a == 2 :
    employes.append(input("entrer l'emloye que vous voullez ajouter :"))  
elif a == 3 :
    p = int(input("entrer la matricule de l'emloyee que vous voulez ajouter : "))
    for i in employes :
        if i.mtl == p :
            employes.remove(i)
        else :
            print("la mtl est inconnue!")
elif a == 4 :
    p = int(input("entrer la matricule de l'emloyee que vous voulez modifier : "))
    for i in employes :
        if i.mtl == p :
            c = (input("entrer le champ que vous voullez modifier(en minuscule svp!) : "))
            if c == "nom" :
                i.nom = input("entrer le nouveau nom: ")
            elif c == "date de naissance" :
                i.dateNaissance = input("entrer la nouvelle date: ")
            elif c == "date d'ambauche" :
                i.date = input("entrer la nouvellle date: ")
            elif c == "salaire de  base" :
                i.salaireBase = input("entrer le nouveau salaire")           
        else :
            print("la mtl est inconnue!")
