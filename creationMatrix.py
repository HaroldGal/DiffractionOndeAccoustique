from scipy.sparse import coo_matrix
from numpy import array
from numpy import append as np_app
from math import cos
import numpy as np

def phi():
	return

def f(x,y):
	return cos(x)*cos(y)

def g(x,y):
	return (cos(x)*cos(y)+1)

class Solver:
	def __init__(self, _triangles, _points, _bord_in,_bord_out):
		self.triangles = _triangles
		self.points = _points
		self.bord_in = _bord_in
		self.bord_out = _bord_out

	def creationMatriceMass(self):
		row_ind = []
		col_ind = []
		data = []
		for K in self.triangles:
			(x1,x2,x3) = (self.points[K[0]], self.points[K[1]], self.points[K[2]])
			aireK = abs(((x2[0]-x1[0])*(x3[1]-x1[1]) - (x3[0]-x1[0])*(x2[1]-x1[1]))/2.)
			for i in range(len(K)):
				for j in range(len(K)):
					row_ind.append(K[i])
					col_ind.append(K[j])
					data.append(aireK/12. * (2 if i==j else 1))
		self.M = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()


	# A REVOIR
	def creationMatriceRigidite(self):
		phi = [np.matrix([[-1],[-1]]),np.matrix([[1],[0]]),np.matrix([[0],[1]])]
		row_ind = []
		col_ind = []
		data = []
		for K in self.triangles:
			(x1,x2,x3) = (self.points[K[0]], self.points[K[1]], self.points[K[2]])
			aireK = abs(((x2[0]-x1[0])*(x3[1]-x1[1]) - (x3[0]-x1[0])*(x2[1]-x1[1]))/2.)
			B = 1./(2.*aireK) * np.matrix([[x3[1]-x1[1], x1[1]-x2[1]], [x1[0]-x3[0],x2[0]-x1[0]]])
			transform = B.getT()*B
			for i in range(len(K)):
				for j in range(len(K)):
					row_ind.append(K[i])
					col_ind.append(K[j])
					data.append((aireK * (phi[j].getT() * transform * phi[i])).item(0) )
		self.D = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()

	def creationVecteurB(self):

		self.b = np.zeros(len(self.points))

		for A in self.bord_out:
			(x1,x2) = (self.points[A[0]], self.points[A[1]])
			xm = [(x1[0]-x2[0])/2.0,(x1[1]-x2[1])/2.0]
			taille = np.sqrt((x2[0]-x1[0])**2 + (x2[1]-x1[1])**2)
			quad = taille/6.0 * (g(x1[0],x1[1]) + 4.*g(xm[0],xm[1])+ g(x2[0],x2[1]))
			for i in A:
				self.b[i] = quad

	def solve(self):
		self.U  = np.linalg.solve((self.M+self.D).toarray(), self.b)