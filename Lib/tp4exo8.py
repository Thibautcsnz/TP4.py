dico= {}
dico['firstname'] = 'Thibaut'
dico['name'] = 'COSENZA'
dico['promo'] = '2022'
dico['group'] = 'RT121'

print("Votre nom est {}, votre prenom est {}, vous faites partie de la promotion {} et votre groupe est {}".format(dico['name'], dico['firstname'], dico['promo'], dico['group']))

#################################
tuplets = {
    "name": dico['name'],
    "firstname": dico['firstname'],
    "promo": dico['promo'],
    "group": dico['group']
}
print("Les clés du dictionnaire sont:")
for key, value in tuplets.items():
    print("-" + key)
print("Les valeurs du dictionnaire sont:")
for key, value in tuplets.items():
    print("-"+ value)
print("Les tuplets du dictionnaire sont:")
for key, value in tuplets.items():
    print("-" + "(" + "'"+ key + "'" + "," + value + ")")

############################################
binome = {}
binome['firstname'] = 'Yann'
binome['name'] = 'BLANCK'
binome['promotion'] = '2022'
binome['group'] = 'RT121'

tuplets2 = {
    "name": binome['name'],
    "firstname": binome['firstname'],
    "promotion": binome['promotion'],
    "group": binome['group']
}
print("Les clés du dictionnaires sont:")
for key, value in tuplets.items():
    print(key)
print("Les valeurs du dictionnaires sont:")
for key, value in tuplets.items():
    print(value)
print("Les tuplets du dictionnaires sont:")
for key, value in tuplets.items():
    print(key + ":" + value)


print("Les étudiants formants le binôme sont:")
print("-L'étudiant {} {} du groupe {}".format(dico['name'], dico['firstname'], dico['group']))
print("-L'étudiant {} {} du groupe {}".format(binome['name'], binome['firstname'], binome['group']))
