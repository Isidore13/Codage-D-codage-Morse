#importation du module csv
import csv

#ouverture du fichier csv
mon_fichier = open('liste-morse.csv', 'r')
contenu = csv.reader(mon_fichier, delimiter=';')

#création d'une liste à partir du fichier
liste_morse = []
next(contenu)
for ligne in contenu:
    liste_morse.append(ligne)


#demande auprès de l'utilisateur à propos de ce qu'il souhaite afficher
v=input("Que voulez vous afficher? (1 ➔ L'alphabet morse, 2 ➔ Le moyen mnémotechnique, 3 ➔ La ligne correspondant à une lettre, 4 ➔ Tout) : ")
if v=="3":
    alpha=list(map(chr, range(97, 123)))
    l=input("Quelle lettre voulez-vous? (Veuillez l'indiquer en minuscules): ")
    occ=0
    for i in alpha:
        if i!=l:
            occ+=1
        else:
            print(liste_morse[occ])
elif v=="4":
    print(liste_morse)
else:
    for i in liste_morse:
        if v=="1":
            print(i[1])
        elif v=="2":
            print(i[2])

#fermeture du fichier
mon_fichier.close()
