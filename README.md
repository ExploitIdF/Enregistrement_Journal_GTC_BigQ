# GTC-Tunnels Enregistrements du journal des consignations dans BigQuery
## Journaux de la GTC
La GTC des tunnels comporte des enregistrements assurant une traçabilité sur son fonctionnement et sur les actions d'exploitation.
  Quels sont les documents de références sur ce sujet ?

Le journal le plus riche que l'on identifie à ce stade est le  **journal des consignations**.

Pour permettre d'exploiter les données du journal des consignations de la GTC, dans le cadre d'analyses avec des notebooks ou avec des applications embarquées sur un Smartphone, 
on propose de placer ces données dans une table ***BigQuery***.  
L'objectif est que la table soit alimentée en temps réel depuis la GTC (qui est sur le réseau technique).  

## En quoi consiste le  journal des consignations ?
Les fichiers d'extraction du journal des consignations fournis par Actemium en mai 2024 n'avaient pas tous les mêmes formats 
et les extractions faites avec l'application JASPER ont également un format différent.

Cependant, le format le plus complet contient les champs suivants :  
  "chrono","loglist","evtnumber","name","value","quality","ts","domain","nature","description",
  "alarmlevel","equipement","utilisateur","evenement","etat","variable" 

Il faudra vérifier si cette information est complète, mais cela constitue certainement une bonne base.  
Les analyses montreront sans doute que certains champs ne sont pas utiles et on pourra envisager dans un deuxième temps de filtrer les données envoyées en ligne.

## Prototyque de programme d'alimentation d'une table BigQuery 
Ce programme permet d'ajouter des enregistrements dans la table BigQuery `tunnels-dirif.GTC.Consignations`.  
Le code pourra être intégré dans un programme activé toutes les minutes, sur le réseau technique, 
à la suite d'une requête sélectionnant les données produites par la GTC pendant la dernière minute.

Pour une plus grande flexibilité, on a placé dans un premier temps les fichiers CSV dans ***Cloud Storage***.  
Cela donne l'option de faire tourner le programme depuis Google Cloud Shell ou depuis une autre machine, différente de celle où sont stockés initialement les fichiers à charger dans  ***BigQuery***.

Si le programme est appelé dans ***Google CLoud Shell*** connecté au même projet que ***BigQuery*** et ***Cloud Storage*** 
il n'y a rien de plus à faire en termes d'authentification.

Si le programme est appelé depuis une autre machine, il faut effectuer la procédure d'authentification documentée ici : 
  `https://cloud.google.com/bigquery/docs/authentication#client-libs`





