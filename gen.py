from random import *

debut = ["Qu'est-ce qui est vert et qui tourne en rigolant ?",
         "Pourquoi Mickey Mousse ?",
         "Comment les abeilles communiquent-elles entre elles ?",
         "Qu'est-ce qu'une voyante qui lit dans du sucre en poudre ?",
         "Vous connaissez la blague de la chaise ?",
         "Vous connaissez la blague du nombril ?",
         "Vous connaissez la blague du ouibril ?",
         "C'est un serpent qui fait du vélo.",
         "La culture, c'est comme la cohomologie.",
         "Qu'est-ce qui est jaune, normé et complet ?",
         "C'est un mec qui rentre dans un bar.",
         "Qu'est-ce qu'un homme avec une mitraillette dans un champ de blé ?",
         "Comment font les chasseurs pour attirer les lapins ?",
         "Que disent 2 fantômes quand ils se rencontrent ?",
         "Qu'est-ce qui est vert et qui a 18 trous de balles ?",
         "Qu'est-ce qui est vert, se déplace sous l'eau, et fait « Bzzz » ?",
         "Qu'est-ce qui est vert et se déplace sous l'eau ?",
         "Qu'est-ce qu'une gousse d'ail qui rebondit contre un mur ?",
         "Qu'est-ce qui est rouge et qui commute ?",
         "Qu'est-ce qui s'est passé en 1111 ?",
         "Que fait un poussin de 300 kg ?",
         "Quels fruits trouve-t-on dans une pièce vide ?",
         "Qu'est-ce qui est transparent et qui court dans un pré ?",
         "Quelle est la différence entre un robot et une sauce napolitaine ?",
         "Que crie un escargot sur le dos d'une tortue ?",
         "Pourquoi faut-il fermer un œil quand on vise ?",
         "Comment appelle-t-on un lapin dur d'oreille ?",
         "Qu'est-ce qui mange des carottes et vit sous l'eau ?",
         "Qu'est-ce qu'une limace ?",
         "Que préfèrent les abeilles dans le mariage ?",
         "Quel est le point commun entre un facteur et un jongleur ?",
         "Toc toc ! Qui est là ?",
         "Qu'est-ce qui fait boin-boin ?",
         "Comment appelle-t-on un squelette qui parle ?",
         "Vous connaissez l'histoire de Toto aux toilettes ?",
         "Vous connaissez la blague de la cravate ?",
         "Tu veux une blague vaseuse ?"]

fin = ["Un chou marreur !",
       "Parce que Mario brosse !",
       "Parce que Jacques sonne !",
       "Par e-miel !",
       "Une extra glucide !",
       "Elle est pliante !",
       "Non. Bril !",
       "Oui. Bril !",
       "Il s'aperçoit qu'il a pas de pattes, et alors il tombe.",
       "Moins on en a, plus on l'étale.",
       "Un espace de Bananach.",
       "Il dit « C'est moi ! » mais en fait c'était pas lui.",
       "Un céréale killer !",
       "Ils imitent le cri de la carotte !",
       "On est dans de beaux draps !",
       "Un terrain de golf !",
       "Un chou-marin !",
       "Un chou-marin ruche !",
       "Le retour du jet d'ail !",
       "Une cerise abélienne !",
       "L'invasion des Huns !",
       "PIOU PIOU !",
       "Des mûres et des coings !",
       "Un troupeau de vitres !",
       "Elles sont toutes les deux aux tomates !",
       "« Pas si vite ! »",
       "Parce que si on ferme les deux, on ne voit rien !",
       "LAPIIIIN !",
       "Un lapin aquatique.",
       "Un escargot SDF !",
       "La lune de miel !",
       "Ils ont tous les deux beaucoup d'adresse(s) !",
       "C'est une sucette géante !",
       "Un Banach !",
       "Un os parleur !",
       "On peut pas, il a fermé la porte a clé.",
       "Elle est longue et plate.",
       "Mets tes bottes !"]

def blague(k):
    res = choice(debut)+" "+choice(fin)
    if len(res)<141 :
        return res
    else :
        if k>0 :
            blague(k-1)
        else :
            return "Erreur de génération de la blague"

if __name__ == '__main__':
    print(blague(10))
