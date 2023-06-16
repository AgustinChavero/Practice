import firebase_admin
from firebase_admin import credentials, db, firestore
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(current_dir, "..", "key.json")
cred = credentials.Certificate(key_path)

# Inicializar la aplicación de Firebase
firebase_admin.initialize_app(
    cred, {"databaseURL": "https://practicepython-4e593-default-rtdb.firebaseio.com"}
)

db = firestore.client()

# Verificar conexión exitosa
print("Conexión exitosa a Firebase")
