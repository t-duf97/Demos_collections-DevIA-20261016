#Les dictionnaires

prix = {
    "pomme" : 2.50,
    "banane" : 1.90,
    "orange" : 3.00 
    }

stagiaires = dict(
    prenom="Alice",
    age=28, 
    ville="Charleroi")

depuis_tuples = dict([("a", 1), ("b", 2)])

carres = {n : n**2 for n in range(1, 6)}  #Compréhension de liste

print(carres)

#Acces dans un dictionnaire

print(prix["pomme"])
# print(prix["mangue"]) #KeyError
print(prix.get("mangue", 1)) # None ou clé par défaut si précisée en param

print("pomme" in prix)

#Ajout/modif dans un dict
prix["orange"] = 1.00
prix["kiwi"] = 0.5

print(prix)
prix.update({"mangue" : 5.00, "banane" : 4.00})
print(prix)




#Suppression

# retire = prix.pop("pomme")
# del prix["banane"] 
# print(prix)



#parcourir
print(prix.keys())
print(prix.values())
print(prix.items()) #renvoie les paires clé valeur sous forme de tuples


cours = {
    "Python" : ["Alice", "Marc"],
    "Java" : ["Zoe"],
}

cours["Python"].append("Sam")
cours["Java"].extend(["Lina"])
cours["Javascript"] = ["Sam", "Lina", "Zoe"]

print(cours["Python"])
print(cours["Java"])
print(cours["Javascript"])

employes = [
    {"nom": "Alice", "salaire": 36000, "service": "IT"},
    {"nom": "Sam", "salaire": 45000, "service": "RH"},
    {"nom": "Marc", "salaire": 46000, "service": "IT"},
]

for e in employes:
    print(f" {e['nom']:<6} {e['salaire']} € ({e['service']})")




mots = ["chat", "chien", "chat", "souris", "chat", "chien"]

compteur = {}

for mot in mots : 
    compteur[mot] = compteur.get(mot, 0) + 1
    print(compteur)


