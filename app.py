# le premier app = dossier app, le 2ème = l'instance de app 
# (app = Flask(__name__)  )

# Si jamais problèmes d'import où autre erreur illogique
# taper : ctrl + maj + p et select "Developer: reload window"


from app import app, db

TESTER_RECUPERATION_CONFIG_JSON = False

if __name__ == "__main__":
    if(TESTER_RECUPERATION_CONFIG_JSON):
        config = db.get_db_config("config.json")
        print(config)
    
    print(__name__) # s'affiche si on execute python3 app.py depuis la racine
    app.run(debug = True) #se lance avec "flask run" ou "python3 app.py"


