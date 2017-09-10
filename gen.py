from random import *

debut = ["Qu'est-ce qui est vert et qui tourne en rigolant ?",
         "Pourquoi Mickey Mousse ?",
         "Comment les abeilles communiquent-elles entre elles ?",
         "Qu'est-ce qu'une voyante qui lit dans du sucre en poudre ?",
         "Vous connaissez la blague de la chaise ?",
         "Vous connaissez la blague du nombril ?",
         "Vous connaissez la blague du ouibril ?",
         "C'est un serpent qui fait du vélo.",
         "La culture, c'est comme la cohomologie.",
         "Qu'est-ce qui est jaune, normé et complet ?",
         "C'est un mec qui rentre dans un bar.",
         "Qu'est-ce qu'un homme avec une mitraillette dans un champ de blé ?",
         "Comment font les chasseurs pour attirer les lapins ?",
         "Que disent 2 fantômes quand ils se rencontrent ?",
         "Qu'est-ce qui est vert et qui a 18 trous de balles ?",
         "Qu'est-ce qui est vert, se déplace sous l'eau, et fait « Bzzz » ?",
         "Qu'est-ce qui est vert et se déplace sous l'eau ?",
         "Qu'est-ce qu'une gousse d'ail qui rebondit contre un mur ?",
         "Qu'est-ce qui est rouge et qui commute ?",
         "Qu'est-ce qui s'est passé en 1111 ?",
         "Que fait un poussin de 300 kg ?",
         "Quels fruits trouve-t-on dans une pièce vide ?",
         "Qu'est-ce qui est transparent et qui court dans un pré ?",
         "Quelle est la différence entre un robot et une sauce napolitaine ?",
         "Que crie un escargot sur le dos d'une tortue ?",
         "Pourquoi faut-il fermer un œil quand on vise ?",
         "Comment appelle-t-on un lapin dur d'oreille ?",
         "Qu'est-ce qui mange des carottes et vit sous l'eau ?",
         "Qu'est-ce qu'une limace ?",
         "Que préfèrent les abeilles dans le mariage ?",
         "Quel est le point commun entre un facteur et un jongleur ?",
         "Toc toc ! Qui est là ?",
         "Qu'est-ce qui fait boin-boin ?",
         "Comment appelle-t-on un squelette qui parle ?",
         "Vous connaissez l'histoire de Toto aux toilettes ?",
         "Vous connaissez la blague de la cravate ?",
         "Tu veux une blague vaseuse ?",
         "Qu'est-ce qui est rectangulaire et dans un coin ?",
         "C'est un café qui rentre dans un bar.",
         "Qu'est-ce qui est rouge et a l'odeur de la peinture bleue ?",
         "Avec quoi ramasse-t-on la papaye ?",
         "Comment fait-on pour mettre un éléphant dans un frigo ?",
         "Pourquoi la poule a-t-elle traversé la route ?",
         "Vous connaissez la blague du papier ?",
         "Vous voulez une blague à deux balles ?",
         "Qu'est-ce qui est vert avec une cape ?",
         "Pourquoi n'y a-t-il pas de ballons sur le plateau de Question pour un Champion ?",
         "Qu'est-ce qu'un petit pois qui se bat contre une carotte ?",
         "Qu'est-ce qui n'est pas un steak ?",
         "Quel est le fruit que les poissons aiment le moins ?",
         "C'est l'histoire d'un tétard.",
         "C'est l'histoire d'un arbre.",
         "Pourquoi les phoques nagent-ils dans l'eau salée ?",
         "Comment les toréadors prennent-ils leur café ?",
         "Connaissez vous la tarte mystère ?",
         "Combien de psychanalistes faut-il pour changer une ampoule ?",
         "Qu'est-ce qui est vert avec des roues ?",
         "Comment on fait avancer un cheval communiste ?",
         "Que fait un policier qui tombe dans l'eau ?",
         "Quelle est la différence entre un pigeon ?",
         "Comment appelle-t-on un chien qui a des lunettes ?",
         "Comment se débarrasse-t-on d'un ver solitaire ?",
         "Quelle est la différence entre un babouin et un voleur ?",
         "Comment s'appellerait Han Solo s'il était allemand ?",
         "Savez-vous pourquoi les girafes n'existent pas ?",
         "Qu'est-ce qui est petit et marron ?",
         "Que dit un crapaud météorologue apercevant un nuage au loin ?",
         "Comment appelle-t-on un crapaud religieux ?",
         "Dans quel pays habitent les crapauds ?",
         "Quelle est la nourriture préférée des crapauds ?",
         "À quoi reconnaît-on un pro du self-défense ?",
         "Qui faut-il demander pour ouvrir les portes ?",
         "Qui faut-il demander pour ouvrir illégalement les portes ?",
         "Qui faut-il demander pour ouvrir les portes en politique ?",
         "Que se serait-il passé si la mère de Benjamin Button n'avait pas eu d'enfant ?",
         "Je dois consigner des mesures d'angles 24 fois par jour, qui suis-je ?",
         "Que peut-on faire avec un vélo des années 50 ?",
         "Que dit un marchand de gaufres qui tombe ?",
         "Pourquoi les kangourous n'ont pas de ressorts attachés aux pieds ?",
         "Comment appelle-t-on un dromadaire à trois bosses ?",
         "Que dit un téléphone guerrier qui a une batterie presque vide ?",
         "Pourquoi la chaise est cassée ?",
         "Quel aliment est surtout consommé par le Dr. No ?",
         "Que dit une armoire à glace qui manque de tomber ?",
         "Que dit un paquebot qui quitte le port ?",
         "Quelle est la différence entre un dindon et une pelleteuse ?",
         "Que dit-on d'une tasse de café qui va chez le coiffeur ?",
         "Quelle est la sauce préférée des ours ?",
         "Que dit-on à un pignon de pain mycologue qui a une belle voix quand il chante ?",
         "Vous savez comment on prépare des bananes flambées pour 50 personnes ?",
         "Quel est le jeu préféré des loutres ?",
         "Que dit une biscotte qui boit une tasse de café ?",
         "Pourquoi attacher les boucs entre eux garantit leur défense ?",
         "Monsieur et Madame Eau ont une fille, quel est son nom ?",
         "Monsieur et Madame Lelavevaisselle ont un fils, quel est son nom ?",
         "Il se passe quoi si on mélange du salami espagnol avec du riz italien ?",
         "Que dit un chien qui résout une énigme ?",
         "Pourquoi les chats peuvent travailler sous terre ?",
         "Monsieur et madame Delégumes ont une fille, quel est son nom ?",
         "Quelle est la différence entre un gaz froid et une soupe de tomates ?",
         "Quel accessoire de danse permet d'assassiner deux personnes à la fois ?",
         "Ça fait quoi si on rajoute de la terre à la crème anglaise ?",
         "Quel est le championnat de tennis préféré des clous ?",
         "Que dit-on du nombre pi quand il ne peut se coucher ?",
         "Dans quel type d'école trouve-t-on le plus souvent des guêpes ?",
         "Quel instrument de musique ne peut être utilisé par un nuage de pluie ?",
         "Pourquoi Mickey Mousse ?",
         "Quel objet est le moins efficace pour prendre son poids ?",
         "Comment appelle-t-on une allocution d'un parquet bien entretenu ?",
         "Monsieur et Madame Zotto ont un fils, quel est son nom ?",
         "Quel objet permet la prise de notes quand le pain ne bouge pas ?",
         "Quelle formule faut-il adresser à une personne qui a fêté son anniversaire la veille ?",
         "Pourquoi Harry Potter aime bien la charcuterie ?",
         "Monsieur et madame Inosaure ont un fils. Quel est son nom ?",
         "Quel musicien aime beaucoup donner son avis sur les instruments qu'il a testé ?",
         "Pourquoi le céleri n'est pas une céréale ?",
         "Qu'est-ce qui est vert, qui monte et qui descend ?",
         "Madame et Madame Menfin on un fils. Comment s'appelle-t-il ?",
         "Qu'est-ce qu'une olive dénoyautée ?",
         "Que dit une feuille qui tombe dans un lac ?",
         "Qu'est-ce qu'un kinder surprise sans surprise ?",
         "De quelle couleur sont les petits pois ?",
         "Quelle est la différence entre un diamètre et un rayon ?",
         "Comment sert-on le thé à un martien ?",
         "Quel est le pluriel de « une bière » ?",
         "Pourquoi la roche volcanique est-elle très propre ?",
         "C'est deux chèvres, Babi et Baba, qui sont dans un bateau. Elles tombent à l'eau, que se passe-t-il ?",
         "Comment appelle-t-on une pyramide avec un masque ?",
         "Pourquoi Perrache ne tient pas debout ?",
         "Pourquoi le clown a-t-il des bretelles bleu-blanc-rouge ?",
         "Qu'est-ce qu'un match de foot à deux ?",
         "Comment appelle-t-on un lapin qui fait du stand-up ?",
         "Il y a 5 poussins sur une table (sur un sol capitonné). Tu veux n'en avoir plus que 4, comment fais-tu ?",
         "Que font les sardines le samedi soir ?",
         "Quelles sont les deux sortes d'OVNI ?",
         "Que dit une vache qui prend ses copines en photo ?",
         "Qu'est-ce qu'un steak derrière un arbre ?",
         "J'ai trois têtes, dix bras, quatre jambes et trois pieds. Qui suis-je?",
         "Quelle est la différence entre une autruche et une orange ?",
         "Quel animal peut lire l'avenir ?",
         "Comment faire cuire 9 patates à 3000m d'altitude, sans moyen de faire du feu ?",
         "Pourquoi les chats n'aiment-ils pas l'eau ?",
         "Monsieur et Madame Frigolbeur ont un fils, comment s'appelle-t-il ?",
         "Qu'est-ce qui est jaune et qui attend ?",
         "Comment fait-on pour faire aboyer un chat ?",
         "Pourquoi Napoléon ne voulait-il pas toucher les arbres ?",
         "Que dit le Christ satisfait ?",
         "Que dit un homme d'Église heureux ?",
         "Quel est l'accessoire préféré des chiens guitaristes ?",
         "Comment appelle-t-on une altiste révolutionnaire ?",
         "Comment appelle-t-on un colis de café qui passe par trois bureaux de postes différents pour anonymiser l'expéditeur ?",
         "Pourquoi les mathématicien·ne·s confondent-ils Noël et Halloween ?",
         "Comment sait-on qu'un éléphant est allé dans le frigo ?",
         "Quel est le département qui adhère le plus ?",
         "Qu'est-ce qu'un petit cheval qui chante le disco ?",
         "Quel est le politicien préféré des ours ?",
         "Comment appelle-t-on un hamster de l'espace ?",
         "Monsieur et Madame Talu ont 4 fils, comment s'appellent-ils ?",
         "Que dit-on quant Karl Zéro devient Noir ?",
         "Comment appelle-t-on des algébristes qui sont des personnes peu fréquentables ?",
         "Qu'est-ce que ça fait quand on regarde un angle droit dans un miroir ?",
         "Que s'exclame David Bowie quand son téléphone est enfin rechargé ?",
         "Comment appelle-t-on l'activité qui consiste à manger des spaghettis dans une jeep en Afrique ?",
         "Monsieur et Madame Bertienne ont un fils, comment l'appellent-il ?",
         "Quel est le caillou le plus chill ?",
         "Pourquoi les Bretons sont-ils tous frères ?",
         "Quel est le cocktail le plus baddass ?",
         "Que fait une couverture avocate ?"
         "Qu'est-ce qui est vert et qui pousse au fond du jardin ?",
         "Quel est le comble d'une maison ?"]

fin = ["Un chou marreur !",
       "Parce que Mario brosse !",
       "Parce que Jacques sonne !",
       "Par e-miel !",
       "Une extra glucide !",
       "Elle est pliante !",
       "Non. Bril !",
       "Oui. Bril !",
       "Il s'aperçoit qu'il a pas de pattes, et alors il tombe.",
       "Moins on en a, plus on l'étale.",
       "Un espace de Bananach.",
       "Il dit « C'est moi ! » mais en fait c'était pas lui.",
       "Un céréale killer !",
       "Ils imitent le cri de la carotte !",
       "On est dans de beaux draps !",
       "Un terrain de golf !",
       "Un chou-marin !",
       "Un chou-marin ruche !",
       "Le retour du jet d'ail !",
       "Une cerise abélienne !",
       "L'invasion des Huns !",
       "PIOU PIOU !",
       "Des mûres et des coings !",
       "Un troupeau de vitres !",
       "Elles sont toutes les deux aux tomates !",
       "« Pas si vite ! »",
       "Parce que si on ferme les deux, on ne voit rien !",
       "LAPIIIIN !",
       "Un lapin aquatique.",
       "Un escargot SDF !",
       "La lune de miel !",
       "Ils ont tous les deux beaucoup d'adresse(s) !",
       "C'est une sucette géante !",
       "Un Banach !",
       "Un os parleur !",
       "On peut pas, il a fermé la porte a clé.",
       "Elle est longue et plate.",
       "Mets tes bottes !",
       "Un vilain frigo qui a été puni !",
       "Et plouf !",
       "De la peinture rouge.",
       "Avec une foufourche.",
       "On ouvre le frigo, on met l'éléphant, on ferme la porte.",
       "Pour aller de l'autre côté.",
       "Elle déchire !",
       "Pan pan !",
       "Un concombre imitant Super-Tomate.",
       "Parce que Julien Lepers !",
       "Un bon duel !",
       "Une pastèque !",
       "La pêche !",
       "Il pensait qu'il était tôt, mais en fait il était tard.",
       "Il pensait qu'il était droit, mais en fait il était un peu plié.",
       "Parce que l'eau poivrée les fait éternuer.",
       "Ils prennent leur café olé !",
       "C'est la tarte, taa-tiin !",
       "Un seul, mais il faut que l'ampoule elle-même aie envie de changer.",
       "En criant « Robert Hue ! ».",
       "L'herbe. J'ai menti pour les roues.",
       "« Flic »",
       "Il a une patte plus longue que l'autre, surtout la gauche.",
       "Un optichien !",
       "On en rajoute un deuxième.",
       "Ils ont tous les deux la peau lisse au cul !",
       "Harrisson Volkswagen.",
       "C'est un cou monté !",
       "Un marron !",
       "« Il va pleuvoir, je croa. »",
       "Un croayant.",
       "La Croatie.",
       "Les croassants.",
       "Il a un porte-clés de bras.",
       "Mentine. Parce qu'elle a les clés, Mentine.",
       "Ptomane. Parce qu'il a les clés, Ptomane.",
       "Menceau. Parce qu'il a les clés, Menceau.",
       "Ce serait le vieux pas né.",
       "Un rapport-heure.",
       "Du rétro-pédalage.",
       "« Zut, je me suis gaufré ! »",
       "Parce que ça leur servirait à rien.",
       "Un drodrodromamamadairedairedaire.",
       "Chargez !",
       "Parce qu'un éléphant s'est assis dessus.",
       "Le Jambon, parce que c'est du Jambon No.",
       "« J'ai eu froid ! »",
       "« PWOOOOOOON »",
       "La pelleteuse a un bras pour soulever des trucs. Le dindon fait juste glouglou.",
       "Qu'elle se fait une soucoupe de cheveux !",
       "La béchamiel.",
       "Tu es doué en chant, pignon !",
       "Bah faut brûler un bananier.",
       "La louterie.",
       "Plus grand chose, parce qu'elle a fondu à cause de la chaleur du café.",
       "Parce que ce sont des boucs liés.",
       "Marthe.",
       "David.",
       "Ça fait du chorizotto.",
       "« J'ai vu ce détail, ça m'a mis la puce à l'oreille ! »",
       "Parce qu'ils sont capables de minet.",
       "Julienne.",
       "Aucune, ce sont des gaz pas chauds.",
       "Le tutu. Parce qu'il tue-tue.",
       "De la crème en glaise.",
       "La Coupe des Vis.",
       "Que c'est un pi sans lit.",
       "Dans les écoles dard.",
       "La guitare sèche.",
       "Parce qu'il a mangé un bloc de savon.",
       "Une balance, parce qu'elle pèse personne.",
       "Une cire-conférence.",
       "Harry.",
       "Le cale-pain.",
       "« Bon annivershier ! »",
       "Parce qu'il étudie à BoutDeLard.",
       "Archibald. Parce qu'Archie bat l'dinosaure !",
       "Jean-Sébastien FeedBach.",
       "Parce que la céréale, c'est le riz.",
       "Feur !",
       "Gérard.",
       "Une olive injective !",
       "« J'ai papier ! »",
       "Un kinder injectif, parce que son noyau est réduit à zéro.",
       "Les petits pois sont rouges !",
       "Un rayon.",
       "Sans oublier la soucoupe.",
       "Des haltères. Car une bière désaltère !",
       "Parce qu'elle se lave !",
       "Babi bêle et Baba coule !",
       "Une pyramide déguisée !",
       "Parce que Vaulx-en-Velin La Soie !",
       "Pour que son pantalon ne tombe pas !",
       "La guerre des goals !",
       "Un blagomorphe !",
       "Bah t'en pousses un !",
       "Elles vont en boîte !",
       "L'OVNI tender et l'OVNI true.",
       "Attention, ne bousez plus !",
       "Un steak caché !",
       "Un menteur.",
       "L'une dort debout tandis que l'autre est un agrume.",
       "Une poule de cristal !",
       "On en enlève une, et hop ! Elle sont qu'huit !",
       "Parce que l'eau minérale !",
       "Roméo !",
       "Jonathan !",
       "On lui donne de l'eau, et puis il la boit.",
       "Parce qu'il avait peur des insectes qui mangent l'écorce !",
       "« Jésus content. »",
       "« Jésuite très content. »",
       "La pédale ouah-ouah !",
       "Nathalie Alto !",
       "Un TOR et facteur !",
       "Parce que 31 oct = 25 dec.",
       "Il y a des traces de pas dans le beurre.",
       "La Drôme, car la Drôme adhère !",
       "Poney M !",
       "Jean-Luc Miélenchon !",
       "Un hamstéroïde !",
       "Jean, car 4 Jean Talu c'est trop la classe !",
       "On dit que Karl a bruni !",
       "L'algèbre de Lie de l'humanité !",
       "Un angle gauche !",
       "L'iPhone marche !",
       "Le pastasafarisme !",
       "Basile !",
       "La Roche Posay !",
       "Parce qu'ils ont Quimper !",
       "Le Vin-Diesel on The Rock !",
       "Elle plaid !",
       "Un extraterrestre qui fait caca !",
       "C'est au niveau du grenier !"]


def blague(k):
    res = choice(debut)+" "+choice(fin)
    if len(res)<141 :
        return res
    else :
        if k>0 :
            blague(k-1)
        else :
            return "Erreur de génération de la blague"

def full_corpus():
    f = open('corpus.txt', 'w')
    for x in debut:
        for y in fin:
            f.write(x + ' ' + y + '\n')
    f.close()

if __name__ == '__main__':
    full_corpus()
    print(blague(10))
    print(len(debut),len(fin))
    print(len(fin[-1]))
