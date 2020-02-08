
print("#################################################")
print("######## Multiplication de deux nombres #########")
print("#################################################")
print(" ")
print(" ")


class Calcul:




def Multiplication(cn,ch):

	nbreB = cn* ch
	print("voici",nbreB) 

	for i in [1,2]:
		print(" ")
		print("Veuillez entrer un nombre quelconque")
		ch = input()
		print("Veuillez entrer le second nombre:")
		cn = input()
		if (ch.isdigit() and cn.isdigit() ):
			#break
			Multiplication(cn,ch)
			print("tata")
		else: print("ce ne sont pas des nombres") 

		

def Multiplication(cn,ch):

	nbreB = cn* ch
	print("voici",nbreB) 
