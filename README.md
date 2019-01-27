# DiffractionOndeAccoustique
L'objectif du projet était de modéliser la diffraction d'une onde acoustique par un sous marin.
## Auteurs
Harold Gallice et Kayim Said Bacar
## Organisation 
Dans ce repertoire vous trouverez trois programmes principaux piloté par un fichier main. Ainsi on trouvera le fichier **LectureFichier** servant à initialiser la liste des triangles du maillage ainsi que la liste des points à partir d'un fichier msh. Un fichier **creationMatrix** qui va créer toutes les matrices au sein d'une classe nommé *Solver* et qui va résoudre le système pour determiner la solution de notre problème. En dernier lieu nous avons le fichier **creationFileParaview** qui va générer un output destiné à Paraview ainsi qu'une image qui correspond au screenshot de la vue de Paraview. Les fichiers générés seront stocké dans un dossier **OutputVtu**
En plus des différents programmes on trouvera un dossier **maillage** qui va contenir notre sous-marin au format geo ainsi que son maillage au format msh. On trouvera également dans ce dossier des programmes destinés à FreeFem++ pour vérification de nos résultats.

## Lancement
Pour utiliser nos programmes, il faut lancer le main avec 3 arguments dont 2 optionnels :

##### Premier argument correspondant à ce que l'on souhaite générer : 
###### 1 : Génère pour un nombre d'onde k fixé, plusieurs output en faisant varier l'angle d'incidence *alpha* entre 0 et 2 *Pi*
###### 2 : Génère pour un angle d'incidence fixé, plusieurs output en faisant varier l'angle d'incidence k entre 0.5 et 4
###### 0 : Génère un seul output pour un angle et un nombre d'onde donné en arguments optionnels.

##### Dans le cas 0 le deuxième argument est k
##### Dans le cas 0 le troisième argument est *alpha*
