# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0;
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants
notes = []

result = 0

for i in range(nombreEtudiants):
    notes.append(float(input(f"Note de l'étudiant {i} : ")))

for i in range(nombreEtudiants):
    result = notes[i] + result
    moyenne = result/nombreEtudiants

print(f"\nMoyenne de classe : {round(moyenne,2)}\n")

print("Numéro de l’Etudiant | note | ecart a la moyenne")

for i in range(nombreEtudiants):
    print(f"{i} | {notes[i]} | {round((notes[i]-moyenne),2)}")