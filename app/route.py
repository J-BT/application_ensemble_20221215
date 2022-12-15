from flask import render_template, request, redirect, url_for
from app import app
from .db import get_db_config, db_connect
import mysql.connector
import requests # <- ne pas installer 


# Afficher les valeurs utilisateurs dans le tableau puis db
# Mettre le cemin absolu de votre config.json
path = "/ISEN_Projects/Flask_WebScrapping/appli_ensemble/config.json"
config = get_db_config(path)

myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()


@app.route('/', methods=["GET", "POST"])   # == @app.route('/index')
def index():

    if request.method == "GET":

        try:
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

        try:
            prenom = request.form["prenom"]
            nom = request.form["nom"]
            adresse_mail = request.form["adresse_mail"]

            query=f"""
                INSERT INTO Utilisateur (nom, prenom, adresse_email) VALUES ("{nom}", "{prenom}", "{adresse_mail}");
            """
            cursor.execute(query)
            myDB.commit()
            
            return redirect(url_for("index"))

        except mysql.connector.Error as e:
            return redirect(url_for("index"), error=e)
