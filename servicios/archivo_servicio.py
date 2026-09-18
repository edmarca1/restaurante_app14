import json
import os

class ArchivoServicio:
    @staticmethod
    def leer_json(ruta_archivo):
        if not os.path.exists(ruta_archivo):
            return []
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    @staticmethod
    def guardar_json(ruta_archivo, datos):
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
