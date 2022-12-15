from app import app

if __name__ == "__main__":
    print(__name__) # s'affiche si on execute python3 app.py depuis la racine
    app.run(debug = True)

