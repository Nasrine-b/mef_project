# Projet MEF (Maillage éléments finis)
Ce répertoire git contient le travail de : *Bartolomé Heulin* et *Nasrine Bahria*, élèves en 5ème année d'école d'ingénieurs en spécialité mathématiques appliquées et informatique. Le projet consiste à mettre en place un solveur de la méthode des éléments finis en `python`.  
Le problème consiste à modéliser la diffusion de la chaleur dans un appartement contenant des radiateurs et des fenêtres.
L'appartement est comme suit :  
![Image de l'appartement](https://bthierry.pages.math.cnrs.fr/course-fem/_images/2020-2021-flat.svg)  
Le problème est noté comme suit :
![Le système](img/systeme.png)


Pour exécuter notre solveur, il faut taper cette commande :
python3 solveur.py [finesseMaillage]

avec finesseMaillage peut prendre les valeurs {0.1, 1, 100}
