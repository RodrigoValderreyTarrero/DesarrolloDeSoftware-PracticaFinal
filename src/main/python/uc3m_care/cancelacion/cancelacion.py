"""Cancelacion"""
import os
from uc3m_care.parser.json_parser import JsonParser
from uc3m_care import JSON_FILES_PATH
from uc3m_care.storage.json_store import JsonStore

class Cancelacion:
    """Cancelacion"""
    class __Cancelacion:
        def __init__(self):
            pass
        @staticmethod
        def escribir_cancelacion(data_list, ruta):
            """Escribe la cancelacion"""
            fichero = JsonStore()
            fichero._FILE_PATH = ruta
            fichero._data_list = data_list
            fichero.save()
        @staticmethod
        def cambiar_tipo_cancelacion(comprobacion):
            """Pasa de Temporal a Final"""
            # Se quiere cambiar la cancelación de la cita a final.
            ruta = JSON_FILES_PATH + 'store_canceled.json'
            lectura_cancelacion = JsonParser(ruta)
            lectura_cancelacion.load_json_content()
            data_list = lectura_cancelacion.json_content
            if os.path.isfile(ruta):
                os.remove(ruta)
            for n_n in data_list:
                if n_n["date_signature"] == comprobacion.date_signature:
                    n_n["cancelation_type"] = 'Final'
            return data_list, ruta

    instance = None

    def __new__(cls):
        if not Cancelacion.instance:
            Cancelacion.instance = Cancelacion.__Cancelacion()
        return Cancelacion.instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)
