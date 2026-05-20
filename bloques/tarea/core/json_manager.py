import json
import os

class JsonManager:

    @staticmethod
    def load(path):

        # OBTENER CARPETA
        folder = os.path.dirname(path)

        # CREAR CARPETA SI NO EXISTE
        if folder and not os.path.exists(folder):

            os.makedirs(folder)

        # CREAR ARCHIVO SI NO EXISTE
        if not os.path.exists(path):

            with open(path, "w", encoding="utf-8") as file:

                json.dump([], file, indent=4, ensure_ascii=False)

            return []

        try:

            # ABRIR ARCHIVO
            with open(path, "r", encoding="utf-8") as file:

                content = file.read().strip()

                # VALIDAR VACIO
                if not content:

                    return []

                # JSON -> PYTHON
                return json.loads(content)

        except (json.JSONDecodeError, FileNotFoundError):

            return []

    @staticmethod
    def save(path, data):

        # OBTENER CARPETA
        folder = os.path.dirname(path)

        # CREAR CARPETA SI NO EXISTE
        if folder and not os.path.exists(folder):

            os.makedirs(folder)

        # GUARDAR JSON
        with open(path, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4, ensure_ascii=False)