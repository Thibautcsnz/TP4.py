m= [5, 2, 4, 8, 1, 3]
for i in range (len(m)):
    for j in range (i+1, len(m)):
        if m[i]> m [j] :
            m[i],m[j]=m[j],m[i]

print(sorted(m))
#sorted n'agit pas sur la liste (affiche juste l'affichage de la list triée)