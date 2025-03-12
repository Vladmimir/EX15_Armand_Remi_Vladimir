from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

# Connexion à la base de données
DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/mydb'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()  # Base pour SQLAlchemy
Session = sessionmaker(bind=engine)

# Définir le modèle pour la table 'index-egalite-fh-utf8'
class IndexEgalite(Base):
    __tablename__ = 'index-egalite-fh-utf8'

    Annee = Column(Integer)
    Structure = Column(Text)
    Tranche_effectifs = Column(Text)
    SIREN = Column(Integer, primary_key=True)  # SIREN comme clé primaire
    Raison_Sociale = Column(Text)
    Nom_UES = Column(Text)
    Entreprises_UES_SIREN = Column(Text)
    Region = Column(Text)
    Departement = Column(Text)
    Pays = Column(Text)
    Code_NAF = Column(Text)
    Note_Ecart_remuneration = Column(Text)
    Note_Ecart_taux_augmentation = Column(Text)
    Note_Ecart_taux_de_promotion = Column(Text)
    Note_Ecart_taux_augmentation2 = Column(Text)
    Note_Retour_conge_maternite = Column(Text)
    Note_Hautes_remunerations = Column(Integer)
    Note_Index = Column(Text)

# Crée la table dans la base de données si elle n'existe pas
Base.metadata.create_all(engine)

# Route de recherche avec tous les paramètres possibles
@app.route('/search-entreprise', methods=['GET'])
def search_entreprise():
    try:
        session = Session()
        
        # Extraire les paramètres de recherche de l'URL (query parameters)
        params = request.args

        # Créer un dictionnaire pour stocker les filtres
        filters = {}
        for key, value in params.items():
            filters[key] = value

        # Construire la requête avec les filtres dynamiques
        query = session.query(IndexEgalite)
        
        # Appliquer les filtres à la requête
        for field, value in filters.items():
            # On utilise `getattr()` pour accéder dynamiquement aux champs de l'objet
            query = query.filter(getattr(IndexEgalite, field).like(f"%{value}%"))

        # Récupérer les résultats
        entreprises = query.all()

        # Si des entreprises sont trouvées
        if entreprises:
            result = []
            for entreprise in entreprises:
                result.append({
                    'SIREN': entreprise.SIREN,
                    'Raison Sociale': entreprise.Raison_Sociale,
                    'Nom UES': entreprise.Nom_UES,
                    'Region': entreprise.Region,
                    'Departement': entreprise.Departement,
                    'Pays': entreprise.Pays,
                    'Code NAF': entreprise.Code_NAF,
                    'Note Index': entreprise.Note_Index
                })
            return jsonify(result)
        else:
            return jsonify({'message': 'Aucune entreprise trouvée avec ces critères'}), 404
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
