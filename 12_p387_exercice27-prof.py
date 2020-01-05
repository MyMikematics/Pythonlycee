#-*- coding:utf8 -*-
# Python 3

# travail sur les listes

L = ['c', 'e', 'c', 'l', 'j', 'd']

# remplacer 'j' par 'i' dans L
L[4] = 'i' # on a compté pour trouver le rang de 'j'
# autre idée
L[L.index('j')] = 'i' # index renvoie le rang du premier 'j' trouvé



# échanger première et dernière valeur
# méthode classique
prem = L[0]
der = L[len(L)-1]
L[0] = der
L[len(L)-1] = prem
 
# méthode "à la Python" avec les affectations en parallèle
 L[0], L[len(L)-1] = L[len(L)-1], L[0]
 
 
 
# changer la casse
la fonction upper() met une lettre en majuscule.
for i in range(len(L)):
	L[i] = L[i].upper()
