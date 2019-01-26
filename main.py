from LectureFichier import lectureFichier
from creationMatrix import Solver
from creationFileParaview import createVisu
import numpy as np
import sys
liste_position,liste_triangle,bords_in,bords_out=lectureFichier("maillage/easySurf.msh")
Elem = Solver(liste_triangle,liste_position,bords_in,bords_out)
#a = Solver([[2,1,0]],[[0.,0.],[1.0,0.],[0.,1.0]],bords,bords)
#Elem.creationMatriceMass()
alpha=np.pi
k=10
if (len(sys.argv)==3):
	k=float(sys.argv[1])
	alpha=float(sys.argv[1])

Elem.creationMatriceMasseHelmholtz(k,alpha)
Elem.creationMatriceMasseBordHelmholtz(k,alpha)
Elem.creationMatriceRigidite()
#Elem.creationVecteurB()
Elem.creationVecteurBHelmholtz(k,alpha)
Elem.creationMatriceAHelmholtz()
Elem.newsolve(k,alpha)
createVisu(Elem.U, liste_position,liste_triangle)