# GTC-Tunnels Enregistrements du journal des consignations dans BigQuery
Pour permettre d'exploiter les données de la table des consignations de la GTC, dans le cadre d'analyses avec des notebooks ou avec des applications embarquées sur un Smartphone, 
on propose de placer ces données dans une table ***BigQuery***.  
L'objectif est que la table soit alimentée en temps réel depuis la GTC (sur le réseau technique).  

Ce programme permet d'ajouter des enregistrements dans la table BigQuery `tunnels-dirif.GTC.Consignations`.  
Le code pourra être intégré dans un programme activé toutes toutes les minutes, sur le réseau technique, à la suite d'une requête sélectionnant les données produites par la GTC pendant la dernière minute.

Pour une plus grande flexibilité, on a placé dans un premier temps les fichiers CSV dans ***Cloud Storage***.  
Cela donne l'option de faire tourner le programme depuis Cloud Schell ou depuis une autre machine, différente de celle où sont stockés initiailement les fichiers à charger dans  ***BigQuery***.

Si le programme est appelé dans ***Google CLoud Shell*** connecté au même projet que ***BigQuery*** et ***Cloud Storage*** il n'y a rien de plus à faire en termes d'authentification.

Si le programme est appelé depuis une autre machine, il faut efectuer la procédure d'authentification documentée ici :`https://cloud.google.com/bigquery/docs/authentication#client-libs`




