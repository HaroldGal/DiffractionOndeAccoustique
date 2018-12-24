dicodesTriangles={}
fichier = open("maillage/easySurf.msh","r") 
liste_lines=fichier.readlines()
compteur=0
while liste_lines[compteur].rstrip("\n\r")!='$Nodes': 
	compteur=compteur+1

# on se place sur la liste des nodes

nb_point=int(liste_lines[compteur+1].rstrip("\n\r"))
liste_position=[]
for i in range(compteur+2,nb_point+compteur+2):
	position_courante=map(float, liste_lines[i].split(' '))
	tuple_temp=(position_courante[1],position_courante[2],position_courante[3])
	liste_position.append(tuple_temp)

debuttriangle=nb_point+compteur+4
nb_triangle=int(liste_lines[debuttriangle].rstrip("\n\r"))
liste_triangle=[]
for i in range(debuttriangle+1,debuttriangle+nb_triangle+1):
	position_courante=map(int, liste_lines[i].split(' '))
	#decalage de 1 de la numérotation initiale , on consdiere qu'il y a un sommet 0
	tuple_temp=(position_courante[5]-1,position_courante[6]-1,position_courante[7]-1)
	liste_triangle.append(tuple_temp)