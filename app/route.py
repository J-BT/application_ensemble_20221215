from flask import render_template
from app import app
from .db import get_db_config, db_connect

@app.route('/')   # == @app.route('/index')
def index():

    # Afficher les valeurs utilisateurs dans le tableau puis db
    config = get_db_config("/ISEN_Projects/Flask_WebScrapping/appli_ensemble/config.json")
    
    
    # myDB = db_connect(config)
    # # cursor = myDB.cursor()

    # print("==========" + myDB.is_connected)
    

    # query="""
    #     SELECT * FROM `Utilisateur`;
    # """
    # cursor.execute(query)
    # result_select = cursor.fetchall()

    # print(result_select)
    # # inserer des valeurs utilisateurs dans le tableau puis db

    return render_template('index.html', configHTML=config)

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