i=0
n = int(input("entrer une valeur: "))


case = int(input("\nchoisir un type de boucle\n0:Boucle while\n1:Boucle For \n>:"))
fact=n

if case == 0:
    while i != n-1:
        x = fact
        i = i+1
        fact *= n-i
        print(f"{n-i}*{x} = {fact}")
    print(f"le factoriel de {n} est {fact}")

elif case == 1:
    for i in range(n-1):
        x = fact
        fact *= n-(i+1)
        print(f"{n-(i+1)}*{x} = {fact}")
    print(f"le factoriel de {n} est {fact}")

else:
    case = int(input("\nchoisir un type de boucle\n0:Boucle while\n1:Boucle For \n>:"))