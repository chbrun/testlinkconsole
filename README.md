testlinkconsole
===============

console d'accès testlink

Installation
============
* Cloner le repo
* configuration dans le fichier testlinkclient.cfg l'url d'acces à testlink et la clé d'API (elle se trouve dans le projet)
* Le projet de test sous testlink doit utiliser les variables personnalisés pour les testcase suivantes:
** scriptBehat : type string : va contenir le script behat à lancer automatiquement
** Browsers : type checkbox : sera utiliser par le script pour appeler behat selon le profil. J'utilise un profil par navigateur.

Utilisation
===========
* lancer le script
* utiliser les commandes directement à la console
* utilsier l'aide
* la console utiliser la completion des commandes

Commande à la console
=====================
* help : l'aide
* save : sauvegarde les paramètres dans le fichier cfg
* list : liste les objets de testlink (projets, campagnes, tests)
** A noter que pour lister les campagnes, les tests, il faut setter un projet
* show : affiche les variables de la console
* set  : permet de setter une variable
** Ex : set projetid 1 
* get  : récupère la valeur d'une variable
* run  : lance la campagne de test à condiction d'avoir spécifier le projet et la campagne.

A noter que la console recharge automatiquement le fichier cfg au démarrage, ce qui éviter la fois d'après à revaloriser les variables

