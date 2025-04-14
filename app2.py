from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Connexion à la base de données
DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/mydb'
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()  # Base pour SQLAlchemy
Session = sessionmaker(bind=engine)

# Définir le modèle pour la table 'index-egalite-fh-utf8'
class IndexEgalite(Base):
    __tablename__ = 'index-egalite-fh-utf8'  # Nom de la table dans la BDD

    Annee = Column(Integer)
    Structure = Column(Text)
    Tranche_effectifs = Column("Tranche effectifs", Text)  # Utilisation du nom exact de la colonne avec un espace
    SIREN = Column(Integer, primary_key=True)  # SIREN comme clé primaire
    Raison_Sociale = Column("Raison Sociale", Text)  # Utilisation du nom exact de la colonne avec un espace
    Nom_UES = Column("Nom UES", Text)  # Utilisation du nom exact de la colonne avec un espace
    Entreprises_UES_SIREN = Column("Entreprises UES (SIREN)", Text)  # Utilisation du nom exact de la colonne avec un espace
    Region = Column(Text)
    Departement = Column(Text)
    Pays = Column(Text)
    Code_NAF = Column("Code NAF", Text)  # Utilisation du nom exact de la colonne avec un espace
    Note_Ecart_remuneration = Column("Note Ecart remuneration", Text)  # Utilisation du nom exact de la colonne avec un espace
    Note_Ecart_taux_augmentation = Column("Note Ecart taux augmentation (hors promotion)", Text)  # Utilisation du nom exact de la colonne avec un espace
    Note_Ecart_taux_de_promotion = Column("Note Ecart taux de promotion", Text)  # Utilisation du nom exact de la colonne avec un espace
    Note_Ecart_taux_augmentation2 = Column("Note Ecart taux augmentation", Text)  # Utilisation du nom exact de la colonne avec un espace
    Note_Retour_conge_maternite = Column("Note Retour conge maternite", Text)  # Utilisation du nom exact de la colonne avec un espace
    Note_Hautes_remunerations = Column("Note Hautes remunerations", Integer)  # Utilisation du nom exact de la colonne avec un espace
    Note_Index = Column("Note Index", Text)  # Utilisation du nom exact de la colonne avec un espace

# Crée la table dans la base de données si elle n'existe pas
Base.metadata.create_all(engine)

@app.route('/get-entreprise/<int:siren>', methods=['GET'])
def get_entreprise(siren):
    try:
        session = Session()
        
        # Requête pour récupérer l'entreprise par son SIREN
        entreprise = session.query(IndexEgalite).filter_by(SIREN=siren).first()
        
        # Si l'entreprise existe
        if entreprise:
            return jsonify({
                'SIREN': entreprise.SIREN,
                'Raison Sociale': entreprise.Raison_Sociale,
                'Nom UES': entreprise.Nom_UES,
                'Region': entreprise.Region,
                'Departement': entreprise.Departement,
                'Pays': entreprise.Pays,
                'Code NAF': entreprise.Code_NAF,
                'Note Index': entreprise.Note_Index
            })
        else:
            return jsonify({'message': 'Entreprise non trouvée'}), 404
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500
    finally:
        session.close()

@app.route('/add-entreprise', methods=['POST'])
def add_entreprise():
    try:
        # Extraire les données JSON de la requête
        data = request.get_json()
        
        # Créer une nouvelle instance de l'entreprise avec les données reçues
        new_entreprise = IndexEgalite(
            Annee=data['Annee'],
            Structure=data['Structure'],
            Tranche_effectifs=data['Tranche_effectifs'],
            SIREN=data['SIREN'],
            Raison_Sociale=data['Raison_Sociale'],
            Nom_UES=data['Nom_UES'],
            Entreprises_UES_SIREN=data['Entreprises UES (SIREN)'],
            Region=data['Region'],
            Departement=data['Departement'],
            Pays=data['Pays'],
            Code_NAF=data['Code_NAF'],
            Note_Ecart_remuneration=data['Note_Ecart_remuneration'],
            Note_Ecart_taux_augmentation=data['Note_Ecart_taux_augmentation'],
            Note_Ecart_taux_de_promotion=data['Note_Ecart_taux_de_promotion'],
            Note_Ecart_taux_augmentation2=data['Note Ecart taux augmentation (hors promotion)'],
            Note_Retour_conge_maternite=data['Note_Retour_conge_maternite'],
            Note_Hautes_remunerations=data['Note_Hautes_remunerations'],
            Note_Index=data['Note_Index']
        )
        
        # Créer une session et ajouter l'entreprise à la base de données
        session = Session()
        session.add(new_entreprise)
        session.commit()
        
        return jsonify({'message': 'Entreprise ajoutée avec succès'}), 201
    except Exception as e:
        return jsonify({'message': f'Erreur : {str(e)}'}), 500
    finally:
        session.close()




if __name__ == '__main__':
    app.run(debug=True)
