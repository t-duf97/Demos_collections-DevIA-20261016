# Initialiser une liste (premier type de collections)
courses = ["pain", "lait", "oeufs"]
vide = []
lettres = list("hello")
melange = ["Theo", 14, True, 3.5]

#Accéder aux éléments d'une liste
print(courses[0])
print(courses[-1]) #Renvoie le dernier élément de la liste
print (len(courses))

#Modifier une liste => ELLE EST MUTABLE

courses[1] = "Lait d'amande"
courses.append("farine")
courses.insert(1, "coca")
courses.extend(["cecemel", "telephone"])

#suppression au sein de la liste
courses.remove("Lait d'amande")
supprime = courses.pop(0)
print(supprime)
print(courses)

notes = [12, 15, 0, 9, 20, 4]
notes.sort(reverse=True)
print(sorted(courses, key=str.lower))
print(notes)


a = [1, 2, 3]
b =a[:]
b.append(99)
print(a)
print(b)

#Parcourir une liste
for i in range(10) :
    print(i)
#for i in range(debut, fin, pas)

for article in courses :
    print("-", article)

for i in range (len(courses)) : 
    print (courses[i])

for i, article in enumerate(courses, 0) : 
    print (f"{i} = {article}")

print(sum(notes))
print(min(notes))
print(max(notes))