from src import create_app
import os

app = create_app()

if os.path.isfile('./.env'):
    pass
else:
    with open('./.env', mode='x') as f:
        f.write("CLOUD_NAME = '" + os.environ.get('CLOUD_NAME')+ "'\n")
        f.write("API_KEY = '" + os.environ.get('API_KEY') + '\n')
        f.write("API_SECREAT = '" + os.environ.get('API_SECREAT') + "'\n")
        f.write("DATABASE_USER = '" + os.environ.get('DATABASE_USER') + "'\n")
        f.write("DATABASE_PASSWORD = '" + os.environ.get('DATABASE_PASSWORD') + "'\n")
        f.write("DATABASE_NAME = '" + os.environ.get('DATABASE_NAME') + "'\n")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
