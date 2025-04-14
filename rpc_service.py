#!/usr/bin/env python3
from xmlrpc.server import SimpleXMLRPCServer
import mysql.connector
import logging

# Configurer le logging pour voir les requêtes
logging.basicConfig(level=logging.INFO)

# Configuration de la connexion à la base de données
db_config = {
    'host': '10.74.16.151',
    'user': 'root',
    'password': 'root',
    'database': 'mydb',
    'charset': 'utf8mb4'  # Ajout pour forcer l'encodage en UTF-8
}

# Fonction pour récupérer les données par SIREN
def get_data_by_siren(siren):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM `index-egalite-fh-utf8` WHERE SIREN = %s"
        cursor.execute(query, (siren,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result:
            logging.info(f"Données trouvées pour le SIREN {siren}")
            # Forcer l'encodage des chaînes en UTF-8
            return {k: v.decode('utf-8') if isinstance(v, bytes) else v for k, v in result.items()}
        else:
            logging.warning(f"SIREN {siren} non trouvé")
            return {"error": "SIREN non trouvé"}
    except Exception as e:
        logging.error(f"Erreur lors de l'accès à la BDD : {e}")
        return {"error": str(e)}


# Création du serveur XMLRPC
def main():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000), logRequests=True)
    server.register_function(get_data_by_siren, "get_data_by_siren")
    print("Service RPC lancé sur le port 8000...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du service RPC.")

if __name__ == "__main__":
    main()
