# 2 - Les ensembles / sets

fruits = {"pomme", "banane", "kiwi", "pomme"} #Pourquoi pas d'ordre?
depuis_liste = set([1, 2, 3, 2, 3, 5, 4, 1])
#depuis_tableau = set([["Coca", 2], ["eau", 3], ["cafe", 4], ["Coca", 3], ["coca", 3]])
print(depuis_liste)
#print(depuis_tableau)
print(fruits)

#Ajouter, supp...
fruits.add("poire")
fruits.discard("mangue") #Ca compile quand meme 
fruits.remove("banane") #Ca renvoie KeyError si jamais pas présent. 



python_grp = {"Alice", "Marc", "Zoe", "Sam"}
java_grp = {"Marc", "Zoe", "Lina"}

#print(python_grp.union(java_grp))
#print(python_grp.intersection(java_grp)) # Les éléments communs aux deux ensembles
print(python_grp.symmetric_difference(java_grp))
print(python_grp)
print(java_grp)
