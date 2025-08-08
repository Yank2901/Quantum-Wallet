from fastapi import FastAPI

# Impostamos las funciones que creamos en nuestro modulo de seguridad
from . import security

# Creamos la instancia de la aplicacion FastAPI
app = FastAPI()

# Definimos el primer "endpoint"
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Qunatum Wallet"}

# --- Bloque de prueba para verificar que el hashing funciona ---
# Esto se imprimirá en tu terminal cuando inicies el servidor
print("--- Probando la lógica de seguridad ---")
password_original = "miClave123"
password_hasheada = security.get_password_hash(password_original)
print(f"La contraseña '{password_original}' se convierte en el hash: {password_hasheada}")
print(f"¿La verificación con la contraseña correcta es exitosa?: {security.verify_password(password_original, password_hasheada)}")
print(f"¿La verificación con una contraseña incorrecta falla?: {not security.verify_password('incorrecta', password_hasheada)}")
print("---------------------------------------")