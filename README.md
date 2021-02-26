<style TYPE="text/css">
code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
    }
});
MathJax.Hub.Queue(function() {
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-AMS_HTML-full"></script>


# Projet MEF (Maillage éléments finis)
Ce répertoire git contient le travail de : Bartolomé Heulin et Nasrine Bahria, élèves en 5ème année d'école d'ingénieurs en spécialité mathématiques appliquées et informatique. Le projet consiste à mettre en place un solveur de la méthode des éléments finis en `python`.  
Le problème consiste à modéliser la diffusion de la chaleur dans un appartement contenant des radiateurs et des fenêtres.
L'appartement est comme suit :  
![Image de l'appartement](https://bthierry.pages.math.cnrs.fr/course-fem/_images/2020-2021-flat.svg)  
Le problème est noté comme suit :  
\\[f(x) = x^2\\]
