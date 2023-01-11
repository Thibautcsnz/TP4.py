binome = ("thibaut", "yann")

print(f"Notre binome est composées de {binome[0]} et {binome[1]}")

#####################################
bi=list(binome)
bi[1] = input("Qui est le nouveau binome?:")
binome = tuple(bi)
print(f"L'étudiant {binome[0]} est en binome avec {binome [1]}")
####################################
bi=list(binome)
del bi[1]
binome = tuple(bi)
print(binome)
####################################
binome = ("yann", "Thibaut")
bi = list(binome)
bi.append(input("Entre le prénom de la troisième personne :"))
binome = tuple(bi)
print(binome)

