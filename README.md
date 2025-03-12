# EX15_Armand_Remi_Vladimir

Documentation rapide
1. Service RPC
J'ai créé un service RPC qui permet de récupérer des données de l'Index EgaPro en utilisant un numéro SIREN. Ce service fonctionne sur le port 8000.

Fonctionnement
J'envoie une requête avec un numéro SIREN.
Le serveur interroge la base de données et renvoie les données correspondantes sous forme de XML.
Comment utiliser
Clone le dépôt.
Lance le fichier rpc_service.py avec la commande :
bash
Copier
Modifier
python rpc_service.py
Le service est maintenant disponible sur http://localhost:8000.
2. API REST avec Swagger

J'ai aussi développé une API REST qui permet d'obtenir les mêmes données que le service RPC, mais au format JSON.

Fonctionnement
J'envoie une requête GET avec un numéro SIREN sur l'endpoint /api/egapro/{siren}.
Le serveur renvoie les données sous forme de JSON.
Swagger
La documentation est disponible à l'adresse http://localhost:5000/swagger pour tester l'API.


<<<<<<< HEAD

# Diagramme de Séquence

diagramme illustre la communication entre un client, un serveur RPC et un serveur REST pour récupérer des données depuis une base de données. Le client envoie une requête (par SIREN) et reçoit la réponse sous différents formats : XML pour RPC et JSON pour REST.

![Diagramme de Séquence](https://www.planttext.com?text=VL4nRiCm3Dm5w0z4fcR81p84WUCCwP0MzWjOcmWCA59AKGRoexZVqCSgsQupDG940kBTyKZjlI1Bk1gji177S30TMT4gXKxkiAg9UmeCrUTX1UXpVXOBz0GjGUciZGFv4L4MMcarwS1cbnbREDhUTGG6WUaxn1-X_0xOKmE6u8QCr_WG9gXFrV6iLQx-aQiuDE4M7wdw2biMMpXP8MPt6LjzpVRQsTxIRkQLnRC5pGOJYkFWWn4KlqXFqsIOkC1smYsoR-_rntcTfqOZapXOPq7OXJuEMa4w_oc5T9FbjEEyrrQhVOhZX_m2)
=======
![image](https://github.com/user-attachments/assets/de665a99-d8d6-44f7-9f2d-196ff4b04fdd)
>>>>>>> d4db3905a224edef05556ecf3df2c3547b4e0cfd










