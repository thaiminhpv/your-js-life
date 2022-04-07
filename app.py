from src import create_app
import os

app = create_app()

if os.path.isfile('./.env'):
    pass
else:
    with open('./.env', mode='x') as f:
        f.write("CLOUD_NAME = '" + input("CLOUD_NAME =")+ "'\n")
        f.write("API_KEY = '" + input("API_KEY =") + '\n')
        f.write("API_SECREAT = '" + input("API_SECREAT =") + "'\n")
        f.write("DATABASE_HOST = '" + input("DATABASE_HOST =") + "'\n")
        f.write("DATABASE_USER = '" + input("DATABASE_USER =") + "'\n")
        f.write("DATABASE_PASSWORD = '" + input("DATABASE_PASSWORD =") + "'\n")
        f.write("DATABASE_NAME = '" + input("DATABASE_NAME =") + "'\n")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
