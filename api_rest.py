from flask import Flask, jsonify, request
from flasgger import Swagger
import mysql.connector
import logging

# Initialisation de Flask et Swagger
app = Flask(__name__)
swagger = Swagger(app)

# Configuration de la connexion à la base de données
db_config = {
    'host': '10.74.16.151',
    'user': 'root',
    'password': 'root',
    'database': 'mydb'
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
            return result
        else:
            logging.warning(f"SIREN {siren} non trouvé")
            return {"error": "SIREN non trouvé"}
    except Exception as e:
        logging.error(f"Erreur lors de l'accès à la BDD : {e}")
        return {"error": str(e)}

# Définition du point d'entrée de l'API REST
@app.route('/egapro', methods=['GET'])
def get_egapro_data():
    """
    Récupérer les données de l'Index EgaPro par SIREN
    ---
    parameters:
      - name: siren
        in: query
        type: string
        required: true
        description: Le numéro SIREN de l'entreprise
    responses:
      200:
        description: Données de l'entreprise
        schema:
          id: EgaPro
          properties:
            SIREN:
              type: string
              example: "123456789"
            data:
              type: object
              example: {"key1": "value1", "key2": "value2"}
      404:
        description: Entreprise non trouvée
    """
    siren = request.args.get('siren')
    if not siren:
        return jsonify({"error": "SIREN est requis"}), 400

    data = get_data_by_siren(siren)
    if "error" in data:
        return jsonify(data), 404

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
