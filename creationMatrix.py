from scipy import sparse

def creationA(Triangles, Points):
	A = sparse.lil_matrix((range(Points), range(Points)))
	for K in Triangles:
		for i in range(K):
			for j in range(K):
				A[i,j] += a_{p}(phi_J, phi_I) // forme a(.,.) restreinte au triangle K_p

		  B[i] += l_{p}(phi_I)$ // forme l(.) restreinte au triangle K_p


if __name__ == 'main':
	creationA([],[])
