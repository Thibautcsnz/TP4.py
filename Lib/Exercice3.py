nMax = 10
prsc = 0
v1 = []
v2 = []
n = 0
i = 0
while n<1 or n>nMax:
    n = int(input("Quel est la taille de vos vecteurs [entre 1 et 10] ? "))
print("\nSaisie du premier vecteur :")

while i !=n:
    v1.append(int(input(f"v1[{i}] =")))
    i = i+1
print("\nSaisie du second vecteur :")
i = 0
while i !=n:
    v2.append(int(input(f"v2[{i}] =")))
    i = i+1

for i in range(n):
    prsc = prsc+(v1[i]*v2[i])
print(f"\nLe produit scalaire de v1 par v2 vaut {prsc}" )