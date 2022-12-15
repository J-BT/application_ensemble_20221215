from flask import render_template
from app import app
from .db import get_db_config, db_connect
import mysql.connector


@app.route('/')   # == @app.route('/index')
def index():

    # Afficher les valeurs utilisateurs dans le tableau puis db
    # Mettre le cemin absolu de votre config.json
    path = "/ISEN_Projects/Flask_WebScrapping/appli_ensemble/config.json"
    config = get_db_config(path)
    
    try:
        myDB = db_connect(config)
        cursor = myDB.cursor()
        dbOK = myDB.is_connected()
        
        query="""
            SELECT * FROM `Utilisateur`;
        """
        cursor.execute(query)
        result_select = cursor.fetchall()

        print(result_select)

        return render_template('index.html', configHTML=config, dbOK__=dbOK)
    
    except mysql.connector.Error as e:
        return render_template('index.html', configHTML=config, error=e)

    # inserer des valeurs utilisateurs dans le tableau puis db

    

"""
On veut une table : Utilisateur
id
nom
prenom
adresse_email

bdd : 151222
user : jib
pwd : 1234
host : localhost
table : Utilisateur

SELECT * FROM `Utilisateur`

INSERT INTO Utilisateur (nom, prenom, adresse_email) VALUES ("Jean", "Edouard", "je@gmail.com");
"""