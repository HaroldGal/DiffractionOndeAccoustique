dicodesTriangles={}
fichier = open("maillage/easySurf.msh","r") 
liste_lines=fichier.readlines()
compteur=0
while liste_lines[compteur].rstrip("\n\r")!='$Nodes': 
	compteur=compteur+1

# on se place sur la liste des nodes

