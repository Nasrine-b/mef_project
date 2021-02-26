from assembly import *

filename = ""

if len(sys.argv) == 1:
	print("[ERREUR] Il manque un argument. Les valeurs possibles sont 0.1, 1 et 100")
	sys.exit()
else:
	if sys.argv[1] == "100":
		filename = "../mesh/problem_100.msh"
	elif sys.argv[1] == "1":
		filename = "../mesh/problem_1.msh"
	elif sys.argv[1] == "0.1":
		filename = "../mesh/problem_0.1.msh"
	else:
		print("[ERREUR] "+sys.argv[1]+" n'est pas un argument valide")
		print("Les argument valide sont 0.1, 1 et 100.")
		sys.exit()

#   Fonction pour la condition de Dirichlet (fenêtre)
def g_fenetre(x,y):
 return -10
#   Fonction pour la condition de Dirichlet (Radiateur)
def g_radiateur(x,y):
 return 25

#   Déclaration des différents tag
tag_piece = 1
tag_rad = 2
tag_fen = 3

#   Initialisation du mesh
gmsh.initialize()
msh = Mesh()
msh.GmshToMesh(filename=filename)
t = Triplet()

#   Calcul de la matrice de rigidité (la matrice de masse est nulle dans notre problème)
Rigidite(msh,2, tag_piece,t)
#   Calcul du second membre
b = np.zeros(msh.npts)
Integrale(msh,2,tag_piece,f,b,2)
#   Conditions de Dirichlet
Dirichlet(msh,1, tag_fen, g_fenetre, t,b)
Dirichlet(msh,1, tag_rad, g_radiateur, t,b)

#   Résolution
A = coo_matrix(t.data).tocsr()
U = linalg.spsolve(A,b)

#   Visualisation
x = [point.x for point in msh.listPoint]
y = [point.y for point in msh.listPoint]
#   Calcul de la triangulation
connectivity=[]
for tri in msh.listTrig:
    connectivity.append([p.id for p in tri.listPoint])

gmsh.finalize()
#   Plot final
plt.tricontourf(x,y,connectivity,U,12,cmap="Spectral_r")
plt.title("Représentation du système avec h = "+sys.argv[1])
plt.colorbar().set_label("Température")
plt.show()
