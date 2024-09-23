# GTC-Tunnels Enregistrements du journal des consignations dans BigQuery
Pour permettre d'exploiter les données de la table des consignations de la GTC, dans le cadre d'analyses avec des notebooks ou avec des applications embarquées sur un Smartphone, 
on propose de placer ces données dans une table ***BigQuery***.  
L'objectif est que la table soit alimentée en temps réel depuis la GTC (qui est sur le réseau technique).  
Les fichiers d'extraction du journal des consignations fournis par Actemium n'avaient pas tous les mêmes formats et les extractions par JASPER ont également un format différent, mais le format le plus complet contient les champs suivants :  
"chrono","loglist","evtnumber","name","value","quality","ts","domain","nature","description",
"alarmlevel","equipement","utilisateur","evenement","etat","variable"  
Il faudra vérifier si cette information est complète, mais cela constitue certainement une bonne base.  
Les analyses montreront sans doute que certains champs ne sont pas utiles et on pourra envisager dans un deuxième temps de filtrer les données envoyées en ligne.

Ce programme permet d'ajouter des enregistrements dans la table BigQuery `tunnels-dirif.GTC.Consignations`.  
Le code pourra être intégré dans un programme activé toutes les minutes, sur le réseau technique, à la suite d'une requête sélectionnant les données produites par la GTC pendant la dernière minute.

Pour une plus grande flexibilité, on a placé dans un premier temps les fichiers CSV dans ***Cloud Storage***.  
Cela donne l'option de faire tourner le programme depuis Google Cloud Shell ou depuis une autre machine, différente de celle où sont stockés initialement les fichiers à charger dans  ***BigQuery***.

Si le programme est appelé dans ***Google CLoud Shell*** connecté au même projet que ***BigQuery*** et ***Cloud Storage*** 
il n'y a rien de plus à faire en termes d'authentification.

Si le programme est appelé depuis une autre machine, il faut effectuer la procédure d'authentification documentée ici :`https://cloud.google.com/bigquery/docs/authentication#client-libs`





