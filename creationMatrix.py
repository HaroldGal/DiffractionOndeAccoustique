from scipy.sparse import coo_matrix
from numpy import array
from numpy import append as np_app
from math import cos

def phi():
	return

def f(x,y):
	return cos(x)*cos(y)

class Solver:
	def __init__(self, _triangles, _points):
		self.triangles = _triangles
		self.points = _points

	def creationMatriceMass(self):
		row_ind = []
		col_ind = []
		data = []
		for K in self.triangles:
			(x1,x2,x3) = (self.points[K[0]], self.points[K[1]], self.points[K[2]])
			aireK = ((x2[0]-x1[0])*(x3[1]-x1[1]) - (x3[0]-x1[0])*(x2[1]-x1[1]))/2.
			for i in range(len(K)):
				for j in range(len(K)):
					row_ind.append(K[i])
					col_ind.append(K[j])
					data.append(aireK/12. * (2 if i==j else 1))
		self.M = A = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()


	# A REVOIR
	def creationMatriceRigidite(self):
		row_ind = []
		col_ind = []
		data = []
		for K in self.triangles:
			(x1,x2,x3) = (self.points[K[0]], self.points[K[1]], self.points[K[2]])
			aireK = ((x2[0]-x1[0])*(x3[1]-x1[1]) - (x3[0]-x1[0])*(x2[1]-x1[1]))/2.
			for i in range(len(K)):
				for j in range(len(K)):
					row_ind.append(K[i])
					col_ind.append(K[j])
					if i==j==0:
						data.append(2 * aireK)
					elif i==0 or j == 0:
						data.append(-aireK)
					elif i==j:
						data.append(aireK)
					else:
						data.append(0)
		self.D = A = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()

	def creationVecteurB(self):
		wn = 1/6

		ind = []
		data = []
		for K in self.triangles:
			(x1,x2,x3) = (self.points[K[0]], self.points[K[1]], self.points[K[2]])
			detJ = ((x2[0]-x1[0])*(x3[1]-x1[1]) - (x3[0]-x1[0])*(x2[1]-x1[1]))
			for i in range(len(K)):
				row_ind.append(K[i])
				col_ind.append(K[j])
				data.append(1) # NON COMPRIS

if __name__ == '__main__':
	a = Solver([[0,1,2]],[[1.0,5.0],[1.0,2.0],[2.0,4.0]])
	a.creationMatriceMass()
	a.creationMatriceRigidite()
	print(a.D.toarray())
