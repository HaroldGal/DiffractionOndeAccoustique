# -*- coding: utf-8 -*-

from LectureFichier import lectureFichier
from creationMatrix import Solver
from creationFileParaview import createVisu
import numpy as np
import sys
import time
liste_position,liste_triangle,bords_in,bords_out=lectureFichier("maillage/easySurf.msh")
Elem = Solver(liste_triangle,liste_position,bords_in,bords_out)
#a = Solver([[2,1,0]],[[0.,0.],[1.0,0.],[0.,1.0]],bords,bords)
#Elem.creationMatriceMass()
#3 argument 1 si on veut générer pour un seul alpha ou un seul k auquel cas il faut choisir alpha et k, 0 si on veut 0 si on veut plusieurs alpha pour k fixé

alpha=np.pi
k=0.8
if (len(sys.argv)==4):
	k=float(sys.argv[2])
	alpha=float(sys.argv[3])


if (int(sys.argv[1])==2):
	for ki in np.arange(0.5,4,0.1):
		Elem.creationMatriceMasseHelmholtz(ki,alpha)
		Elem.creationMatriceMasseBordHelmholtz(ki,alpha)
		Elem.creationMatriceRigidite()
		#Elem.creationVecteurB()
		Elem.creationVecteurBHelmholtz(ki,alpha)
		Elem.creationMatriceAHelmholtz()
		Elem.newsolve(ki,alpha)
		createVisu(Elem.U, liste_position,liste_triangle,ki,alpha)
	
elif(int(sys.argv[1])==1):
	for alphaI in np.arange(0,2*np.pi,0.1):
		Elem.creationMatriceMasseHelmholtz(k,alphaI)
		Elem.creationMatriceMasseBordHelmholtz(k,alphaI)
		Elem.creationMatriceRigidite()
		#Elem.creationVecteurB()
		Elem.creationVecteurBHelmholtz(k,alphaI)
		Elem.creationMatriceAHelmholtz()
		Elem.newsolve(k,alphaI)
		createVisu(Elem.U, liste_position,liste_triangle,k,alphaI)


else:
	tempsbase=time.time()

	Elem.creationMatriceMasseHelmholtz(k,alpha)
	tempsMasseHelmholtz=time.time()-tempsbase
	
	tempsbase=time.time()
	
	Elem.creationMatriceMasseBordHelmholtz(k,alpha)
	tempsMasseBordHelmholtz=time.time()-tempsbase
	tempsbase=time.time()

	Elem.creationMatriceRigidite()
	tempsRigidite=time.time()-tempsbase
	tempsbase=time.time()

	Elem.creationVecteurBHelmholtz(k,alpha)
	tempsvecteurB=time.time()-tempsbase
	tempsbase=time.time()

	Elem.creationMatriceAHelmholtz()
	tempsMatriceA=time.time()-tempsbase
	tempsbase=time.time()

	Elem.newsolve(k,alpha)
	tempssolve=time.time()-tempsbase
	tempsbase=time.time()

	createVisu(Elem.U, liste_position,liste_triangle,k,alpha)
	tempsVisu=time.time()-tempsbase

	print("tempsMasseHelmholtz =",tempsMasseHelmholtz)
	print("tempsMasseBordHelmholtz =",tempsMasseBordHelmholtz)
	print("tempsMatriceA =",tempsMatriceA)
	print("tempsVecteurB =",tempsvecteurB)
	print("tempsSolve =",tempssolve)
	print("tempsVisu =",tempsVisu)