# Enregistrements du journal des consignations dans BigQuery
Pour permettre d'exploiter les données de la table des consignations GTC, dans le cadre d'analyses avec des notebooks ou sur des applications embarquées sur un Smartphone, 
on propose de placer ces données dans une table BigQuery.  
L'objectif est que la table soit alimentée en temps réel depuis la GTC (sur le réseau technique).  

Ce programme permet d'ajouter des enregistrements dans la table BigQuery tunnels-dirif.GTC.Consognations.  
Il pourra être transposé pour tourner toutes les minutes, sur le réseau technique, à la suite d'une requête sélectionnant les données produites par la GTC pendant la dernière minute.

Pour une plus grande flexibilité, on a placé dans un premier temps les fichiers CSV dans *Cloud Storage*.  
Cela donne l'option de faire tourner le programme depuis Cloud Schell ou depuis un autre machine différente de celle où sont stockés initiailement les fichier à charger.




