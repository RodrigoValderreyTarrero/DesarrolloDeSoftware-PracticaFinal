"""Clase para comprobar"""
import re
from datetime import datetime
from uc3m_care import JSON_FILES_PATH
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException
from uc3m_care.parser.json_parser import JsonParser

class Comprobacion:
    """Clase comprobacion"""
    def __init__(self, input_file):
        self.cambio_temp_final = False
        self.cancelation_type, self.date_signature, self.datos, self.reason = self.sacar_valores(input_file)
        self.comprobar_parametros(self.cancelation_type,self.date_signature,self.reason)
        self.comprobar_administrada(self.date_signature)
        self.comprobacion_cancelacion(self.cancelation_type,self.date_signature)
        self.fecha = self.comprobar_existencia(self.date_signature)
        self.comprobacion_pasada(self.fecha)
    @staticmethod
    def comprobacion_pasada(fecha_en_store):
        """Se comprueba si la fecha ya ha pasado"""
        justnow = datetime.utcnow()
        if fecha_en_store < datetime.timestamp(justnow):
            raise VaccineManagementException("La fecha de la cita es anterior al día de hoy")
    @staticmethod
    def comprobar_existencia(date_signature):
        """Se comprueba si existe la cita"""
        ruta_citas = JSON_FILES_PATH + 'store_date.json'
        lectura_cita = JsonParser(ruta_citas)
        found = False
        lectura_cita.load_json_content()
        contenido = lectura_cita.json_content
        for n_n in contenido:
            if n_n["_VaccinationAppointment__date_signature"] == date_signature:
                found = True
                # Aprovechamos el bucle para sacar la fecha (se usa posteriormente)
                fecha_en_store = n_n["_VaccinationAppointment__appointment_date"]
        if not found:
            raise VaccineManagementException("La cita que se pretende cancelar no existe")
        return fecha_en_store

    def comprobacion_cancelacion(self, cancelation_type, date_signature):
        """Se comprueba si la cancelacion ya habia sido realizada"""
        ruta_cancelados = JSON_FILES_PATH + "store_canceled.json"
        cancelados = JsonParser(ruta_cancelados)
        cancelados.load_json_content()
        for n_n in cancelados.json_content:
            if n_n["date_signature"] == date_signature:
                if (cancelation_type == 'Final' and n_n["cancelation_type"] == 'Final') or (
                        cancelation_type == 'Temporal' and n_n["cancelation_type"] == 'Temporal'):
                    # Esto quiere decir que ya fue cancelada la cita con tipo Final o se pretende pasar de
                    # temporal a temporal (no tiene sentido)
                    raise VaccineManagementException("La vacuna que se pretende anular ya había sido cancelada")
                if cancelation_type == 'Final' and n_n["cancelation_type"] == 'Temporal':
                    # Esto quiere decir que se pretende cambiar de final a temporal
                    self.cambio_temp_final = True
                else:
                    # No se puede pasar una cancelacion de final a temporal
                    raise VaccineManagementException("La vacuna que se pretende anular ya había sido cancelada")
    @staticmethod
    def comprobar_administrada(date_signature):
        """Se comprueba si fue administrada"""
        ruta_vacunados = JSON_FILES_PATH + "store_vaccine.json"
        ya_vacunados = JsonParser(ruta_vacunados)
        ya_vacunados.load_json_content()
        for diccionario in ya_vacunados.json_content:
            if diccionario["_VaccinationLog__date_signature"] == date_signature:
                # Esto quiere decir que ya fue vacunado
                raise VaccineManagementException("La vacuna que se pretende anular ya se ha administrado")
    @staticmethod
    def comprobar_parametros(cancelation_type, date_signature, reason):
        "Funcioón para comprobar parámetros"
        # EXCEPCION 1.1: Se comprueba que date_signature tiene el formato requerido
        expresion = r"^[0-9a-fA-F]{64}"
        resultado = re.compile(expresion)
        comprobar = resultado.search(date_signature)
        if comprobar is None or len(date_signature) != 64:
            raise VaccineManagementException("Firma de la cita invalida")
        # EXCEPCION 1.2: Se comprueba que cancelation_type sea Temporal o Final
        if cancelation_type not in ("Temporal", 'Final'):
            raise VaccineManagementException("Tipo de cancelación erroneo")
        # EXCEPCION 1.3: Se comprueba que la razon de la cancelación tenga una longitud aceptable
        if len(reason) < 2 or len(reason) > 100:
            raise VaccineManagementException("Longitud de la razon invalida")
    @staticmethod
    def sacar_valores(input_file):
        """Saca los valores del json"""
        # En primer lugar extraemos del json_cita los valores que necesitaremos
        parser = JsonParser(input_file)
        parser.load_json_content()
        datos = parser.json_content
        # Una vez datos tiene todos los valores, los metemos en variables
        date_signature = datos[0]["date_signature"]
        cancelation_type = datos[0]["cancelation_type"]
        reason = datos[0]["reason"]
        return cancelation_type, date_signature, datos, reason
