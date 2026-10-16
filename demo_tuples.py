# LES TUPLES
#Initialisation du tuple 
coordonnes = (50.41, 49.1)
personne = "Théo", "Dufrasne", 29
depuis_liste = tuple([1, 2, 3])
print(coordonnes)
print(personne)
print(depuis_liste)

faux = ("bonjour") # simple parenthèses de calcul 
vrai = ("bonjour",) #tuple d'un seul élément

print(type(faux)) #str
print(type(vrai)) #tuple

print(coordonnes[0]) #Acces comme les listes
# coordonnes[0] = 25 IMPOSS TYPEERROR

#Unpacking
prenom, nom, age = personne
print(f"{prenom}, {nom}, {age}")

