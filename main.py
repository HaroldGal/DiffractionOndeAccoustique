from LectureFichier import lectureFichier
from creationMatrix import Solver
from creationFileParaview import createVisu

liste_position,liste_triangle,bords=lectureFichier("maillage/easySurf.msh")
Elem = Solver(liste_triangle,liste_position,bords,bords)
#a = Solver([[2,1,0]],[[0.,0.],[1.0,0.],[0.,1.0]],bords,bords)
Elem.creationMatriceMass()
Elem.creationMatriceRigidite()
Elem.creationVecteurB()
Elem.solve()
createVisu(Elem.U, liste_position,liste_triangle)
