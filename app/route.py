from flask import render_template, request, redirect, url_for
from app import app
from .db import get_db_config, db_connect
import mysql.connector
import requests # <- ne pas installer 

@app.route('/', methods=["GET", "POST"])   # == @app.route('/index')
def index():

    if request.method == "GET":

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

            return render_template('index.html',
            configHTML=config, dbOK__=dbOK, HTML_Result=result_select)
        

        except mysql.connector.Error as e:
            return render_template('index.html', configHTML=config, error=e)

        # inserer des valeurs utilisateurs dans le tableau puis db

    if request.method == "POST":

        prenom = request.form["prenom"]
        nom = request.form["nom"]
        adresse_mail = request.form["adresse_mail"]

        
        return redirect(url_for("index"))


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