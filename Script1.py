#Exo1: vérifier l'age de l'individu, vérifier s'il est majeur

#cas1: si l'age de l'individu n'est pas connu

ageIndividu = input("Veuillez entrer votre age")

#print(ageIndividu)

#print(type(ageIndividu))

# ici nous convertissons la variable ageIndividu en un entier
ageIndividu = int(ageIndividu)

if(ageIndividu >= 18):
	print("Vous etes majeur")

else:
	print("Vous etes mineur")
