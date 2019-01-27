# -*- coding: utf-8 -*-

from LectureFichier import lectureFichier
from creationMatrix import Solver
from creationFileParaview import createVisu
import numpy as np
import sys
liste_position,liste_triangle,bords_in,bords_out=lectureFichier("maillage/easySurf.msh")
Elem = Solver(liste_triangle,liste_position,bords_in,bords_out)
#a = Solver([[2,1,0]],[[0.,0.],[1.0,0.],[0.,1.0]],bords,bords)
#Elem.creationMatriceMass()
#3 argument 1 si on veut générer pour un seul alpha ou un seul k auquel cas il faut choisir alpha et k, 0 si on veut 0 si on veut plusieurs alpha pour k fixé

alpha=np.pi
k=3
if (len(sys.argv)==4):
	k=float(sys.argv[2])
	alpha=float(sys.argv[3])


if (int(sys.argv[1])==1):
	Elem.creationMatriceMasseHelmholtz(k,alpha)
	Elem.creationMatriceMasseBordHelmholtz(k,alpha)
	Elem.creationMatriceRigidite()
	#Elem.creationVecteurB()
	Elem.creationVecteurBHelmholtz(k,alpha)
	Elem.creationMatriceAHelmholtz()
	Elem.newsolve(k,alpha)
	createVisu(Elem.U, liste_position,liste_triangle,alpha)
else:
	for alphaI in np.arange(0,2*np.pi,0.1):
		Elem.creationMatriceMasseHelmholtz(k,alphaI)
		Elem.creationMatriceMasseBordHelmholtz(k,alphaI)
		Elem.creationMatriceRigidite()
		#Elem.creationVecteurB()
		Elem.creationVecteurBHelmholtz(k,alphaI)
		Elem.creationMatriceAHelmholtz()
		Elem.newsolve(k,alphaI)
		createVisu(Elem.U, liste_position,liste_triangle,alphaI)



