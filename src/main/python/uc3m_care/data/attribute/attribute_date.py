"""Classs for the date"""
import re
from datetime import datetime
from uc3m_care.data.attribute.attribute import Attribute
from uc3m_care.exception.vaccine_management_exception import VaccineManagementException



class Date(Attribute):
    """Classs for the attribute age"""
    _validation_error_message = "age is not valid"

    def __init__(self, attr_value):
        self._validate(attr_value)
        self._value = attr_value

    def _validate( self, date: str ) -> str:
        expresion = r"^[0-9]{4}-[0-9]{2}-[0-9]{2}"
        resultado = re.compile(expresion)
        comprobar = resultado.search(date)
        if not comprobar:
            raise VaccineManagementException("Formato de fecha incorrecto")
        # Una vez comprobado que la expresión tiene el formato correcto (un isoformat)
        # Sacamos la fecha diferenciando en dias, año y mes
        ano = int(date[0] + date[1] + date[2] + date[3])
        mes = int(date[5] + date[6])
        dia = int(date[8] + date[9])
        # Comprobamos a continuación que los valores tienen rangos coherentes
        if mes > 12:
            raise VaccineManagementException("Mes no válido")
        if dia > 31 and mes in [1, 3, 5, 7, 8, 10, 12]:
            raise VaccineManagementException("Día no válido")
        if dia > 30 and mes in [2, 4, 6, 9, 11]:
            raise VaccineManagementException("Día no válido")
        # Necesitamos comparar fechas para saber si se puede conceder la cita.
        date_datetime = datetime(ano, mes, dia).timestamp()
        justnow = datetime.utcnow()
        if date_datetime < datetime.timestamp(justnow):
            raise VaccineManagementException("Fecha anterior a la actual")