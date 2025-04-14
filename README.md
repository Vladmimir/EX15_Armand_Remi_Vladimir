# EX15_Armand_Remi_Vladimir
# Service RPC - Distribution des données EgaPro

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
![image](https://github.com/user-attachments/assets/19d92d96-53ae-47fb-8fca-8f2d146450e0)

