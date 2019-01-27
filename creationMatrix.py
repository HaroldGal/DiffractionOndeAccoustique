from scipy.sparse import coo_matrix,csr_matrix
from numpy import array
from numpy import append as np_app
from math import cos,sqrt,sin
from cmath import exp
import numpy as np
#alpha=np.pi/2
#k=50
def uinc(x,y,k,alpha):
	
	return  exp(np.complex(0,1)*k*(x*cos(alpha)+y*sin(alpha)))
	#return sin(k*x/2.0)*sin(k*y/2.0)
class Solver:
	def __init__(self, _triangles, _points, _bord_in,_bord_out):
		self.triangles = _triangles
		self.points = _points
		self.bord_in = _bord_in
		self.bord_out = _bord_out
		self.b=np.zeros(len(_points))

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

	def creationMatriceMasseHelmholtz(self,k,alpha):
		row_ind = []
		col_ind = []
		data = []
		 #nombre onde
		for K in self.triangles:
			
			(x1,x2,x3) = (self.points[K[0]], self.points[K[1]], self.points[K[2]])
			aireK = abs(((x2[0]-x1[0])*(x3[1]-x1[1]) - (x3[0]-x1[0])*(x2[1]-x1[1]))/2.)
			for i in range(len(K)):
				for j in range(len(K)):
					row_ind.append(K[i])
					col_ind.append(K[j])
					mydata=(np.complex(1,0)*k*k*aireK/12. * (2 if i==j else 1))
					data.append(mydata)
		
		self.M = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()
	
	def creationMatriceMasseBordHelmholtz(self,k,alpha):
		row_ind = []
		col_ind = []
		data = []
		#k=50 #nombre onde
		for K in self.bord_out:
			(x1,x2) = (self.points[K[0]], self.points[K[1]])
			sigma = np.sqrt((x2[0]-x1[0])**2 + (x2[1]-x1[1])**2)
			for i in range(len(K)):
				for j in range(len(K)):
					row_ind.append(K[i])
					col_ind.append(K[j])
					mydata=-np.complex(0,1)*k*sigma/6* (2 if i==j else 1)
					data.append(mydata)

		self.Mbord = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()

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
					mydata=(-aireK * (phi[j].getT() * transform * phi[i])).item(0)
					data.append(mydata)
					
			
		self.D = coo_matrix((array(data), (array(row_ind), array(col_ind))), shape=(len(self.points),len(self.points))).tocsr()


	def creationVecteurB(self):

		self.b = np.zeros(len(self.points))

		for A in self.bord_in:
			(x1,x2) = (self.points[A[0]], self.points[A[1]])
			xm = [(x1[0]-x2[0])/2.0,(x1[1]-x2[1])/2.0]
			taille = np.sqrt((x2[0]-x1[0])**2 + (x2[1]-x1[1])**2)
			quad = taille/6.0 * (g(x1[0],x1[1]) + 4.*g(xm[0],xm[1])+ g(x2[0],x2[1]))
			for i in A:
				self.b[i] = quad

	def creationVecteurBHelmholtz(self,k,alpha):

		self.b = np.zeros(len(self.points),np.complex128)

		for aret in self.bord_in:
			(x1,x2) = (self.points[aret[0]], self.points[aret[1]])
			value1=-uinc(x1[0],x1[1],k,alpha)
			value2=-uinc(x2[0],x2[1],k,alpha)
			self.b[aret[0]]=value1
			self.b[aret[1]]=value2

	def creationMatriceAHelmholtz(self):
		Dtemp=(self.M+self.D+self.Mbord).toarray()
		for btest in self.bord_in:
			Dtemp[btest[0],:]=0
			#Dtemp[:,btest[0]]=0
			Dtemp[btest[0],btest[0]]=1
			Dtemp[btest[1],:]=0
			#Dtemp[:,btest[1]]=0
			Dtemp[btest[1],btest[1]]=1
		#data=Dtemp.flatten()
		#(data.shape)
		self.A =csr_matrix(Dtemp)

	def solve(self):
		self.U  = np.linalg.solve((self.M+self.D).toarray(), self.b)

	def newsolve(self,k,alpha):
		#on recupere la solution
		self.U  = np.linalg.solve((self.A).toarray(), self.b)
		#on recree le champ physique en parcourant tous les points
		
		for i  in range(len(self.points)):
			(x1,x2,x3)=self.points[i]
			self.U[i]=abs(self.U[i]+uinc(x1,x2,k,alpha))

