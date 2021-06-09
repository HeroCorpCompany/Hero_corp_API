# HeroCorp_API

## Herocorp
Herocorp est le nom que nous avons donné au projet que nous avons mené pendant deux semaines. Le but était de créer, en java, un monde autonome. Nous nous sommes inspiré du monde présenté dans le webtoon Solo Levelling. A savoir : des donjons apparaissent aléatoirement dans le monde, des chasseurs forment des groupes pour vaincre les monstres qui habitent le donjon et le fermer. Des guildes de chasseurs se forment également.

## API
Nous avons décidé de pousser le sujet un peu plus loin. Quel intérêt d'avoir un monde qui tourne si personne ne sait ce qui s'y passe ? Nous avons donc voulu utiliser d'autres connaissances acquise lors de cette deuxième année à l'Ensai et mettre en place une API qui permettrait à chacun d'accéder aux données de notre monde en temps réel. Pour cela, il a fallu modifier notre monde pour qu'il stocke réguliérement l'état des différents acteurs dans une base de donnée. Ensuite, nous avons créé cett API qui permet de récupérer les données via quelques requêtes.

## Les requêtes
- `/lieux` : Renvoie la liste des lieux actuellement présents dans le monde sous la forme de dictionnaires contenant les clés suivantes : `{"id", "type", "x", "y"}`
- `/guildes/{idGuilde}` : Renvoie les informations de la guilde ayant l'id donné avec les clés suivantes : `{"id", "argent", "recrute}`
- `/monstres/{idDonjon}` : Renvoie les monstres présent dans le donjon ayant l'id donné avec les clés suivantes : `{"id", "nom", "classe", "recompense", "idDonjon"}`
- `/chasseurs/guilde/{idGuilde}` : Renvoie la liste des chasseurs présents dans la guilde ayant l'id donné avec les clés suivantes : `{"id", "nom", "age", "argent", "classe", "salaire", "idGroupe", "idGuilde", "idPosition"}`
- `/chasseurs/lieu/{idLieu}` : Renvoie la liste des chasseurs présents dans le lieu ayan l'id donné avec les clés suivantes : `{"id", "nom", "age", "argent", "classe", "salaire", "idGroupe", "idGuilde", "idPosition"}`