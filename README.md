# EX15_Armand_Remi_Vladimir

=======
# Service RPC Vladimir- Distribution des données EgaPro

Ce projet implémente un service RPC permettant de récupérer les données de l'Index EgaPro en fonction du numéro SIREN.

## Prérequis
- Python 3
- MySQL avec la base de données `mydb`
- Dépendances Python : `mysql-connector-python`

## Installation
1. **Cloner le dépôt et se placer sur la branche `RPC_Vladimir`**
   ```bash
   git clone https://github.com/Vladmimir/EX15_Armand_Remi_Vladimir.git
   cd EX15_Armand_Remi_Vladimir
   git checkout RPC_Vladimir
   ```

2. **Installer les dépendances**
   ```bash
   pip install mysql-connector-python
   ```

3. **Configurer la base de données**  
   Il faut que votre base de données MySQL soit accessible avec :  
   - **IP :** `10.74.16.151`
   - **User :** `root`
   - **Password :** `root`
   - **Base :** `mydb`
   
   Les données sont importées dans la table `index-egalite-fh-utf8`.

## Démarrer le serveur RPC
Lancer le serveur RPC en exécutant :
```bash
python rpc_server.py
```
Le service écoute sur le port `8000`.

## Utilisation du client RPC
Un client peut interroger le serveur comme suit (en ouvrant une autre console python, toujours dans le chemin local du repo):
```python
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000")
result = proxy.get_data_by_siren("423492792")
print(result)
```

Si le SIREN existe, il retourne les informations correspondantes, sinon un message d'erreur est renvoyé. Les accents ne sont pas affichés malgré que l'encodage UTF-8 soit forcé (cela vient de l'import des données dans la BDD)



RPC_Armand

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
api_rest.py

J'ai aussi développé une API REST qui permet d'obtenir les mêmes données que le service RPC, mais au format JSON.

Fonctionnement
J'envoie une requête GET avec un numéro SIREN sur l'endpoint /api/egapro/{siren}.
Le serveur renvoie les données sous forme de JSON.
Swagger
La documentation est disponible à l'adresse http://localhost:5000/swagger pour tester l'API.

#API REST Rémi
api-rest-avec-plusieurs-parametre.py
app2.py
app3.py

# Diagramme de Séquence

diagramme illustre la communication entre un client, un serveur RPC et un serveur REST pour récupérer des données depuis une base de données. Le client envoie une requête (par SIREN) et reçoit la réponse sous différents formats : XML pour RPC et JSON pour REST.

![Diagramme de Séquence](https://www.planttext.com?text=VL4nRiCm3Dm5w0z4fcR81p84WUCCwP0MzWjOcmWCA59AKGRoexZVqCSgsQupDG940kBTyKZjlI1Bk1gji177S30TMT4gXKxkiAg9UmeCrUTX1UXpVXOBz0GjGUciZGFv4L4MMcarwS1cbnbREDhUTGG6WUaxn1-X_0xOKmE6u8QCr_WG9gXFrV6iLQx-aQiuDE4M7wdw2biMMpXP8MPt6LjzpVRQsTxIRkQLnRC5pGOJYkFWWn4KlqXFqsIOkC1smYsoR-_rntcTfqOZapXOPq7OXJuEMa4w_oc5T9FbjEEyrrQhVOhZX_m2)
=======
![image](https://github.com/user-attachments/assets/de665a99-d8d6-44f7-9f2d-196ff4b04fdd)






