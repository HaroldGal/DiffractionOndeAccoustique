from LectureFichier import lectureFichier
from creationMatrix import Solver
from creationFileParaview import createVisu
import numpy as np
liste_position,liste_triangle,bords_in,bords_out=lectureFichier("maillage/easySurf.msh")
Elem = Solver(liste_triangle,liste_position,bords_in,bords_out)
#a = Solver([[2,1,0]],[[0.,0.],[1.0,0.],[0.,1.0]],bords,bords)
#Elem.creationMatriceMass()
Elem.creationMatriceMassTest()
Elem.creationMatriceRigidite()
#Elem.creationVecteurB()
Elem.creationVecteurBtest()
Elem.creationMatriceA()
Elem.newsolve()
print(Elem.U)
createVisu(Elem.U, liste_position,liste_triangle)
print(Elem.bord_in)
print(np.matmul(np.matmul(np.ones(len(liste_position)),Elem.M.toarray()),np.ones(len(liste_position))))
