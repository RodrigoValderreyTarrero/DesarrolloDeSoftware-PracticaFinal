"""Test de control de flujo"""
import os
import unittest
from uc3m_care import JSON_FILES_PATH, JSON_FILES_TESTS_PATH
from uc3m_care import VaccineManagementException
import json
from uc3m_care import VaccineManager
from uc3m_care.parser.json_parser import JsonParser


class TestControlFlujo(unittest.TestCase):
    """Estos tests comprueban el funcionamiento interno de la funcion"""
    def test_formato_de_cita_incorrecto(self):
        """La fecha es incorrecta"""
        # Nos aseguramos de tener en el store_vaccine la única cita que queremos
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_date.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex
        datos_cita = [{
            "_VaccinationAppointment__alg": "SHA-256",
            "_VaccinationAppointment__type": "DS",
            "_VaccinationAppointment__patient_sys_id": "72b72255619afeed8bd26861a2bc2caf",
            "_VaccinationAppointment__patient_id": "78924cb0-075a-4099-a3ee-f3b562e805b9",
            "_VaccinationAppointment__phone_number": "+34123456789",
            "_VaccinationAppointment__issued_at": 2646697600.0,
            "_VaccinationAppointment__appointment_date": 2646697600.0,
            "_VaccinationAppointment__date_signature": "YYYYYYYYEEEE34024932849034843YYYYYFFBJDSLKDLKNFNSLDJNFJLKSNLKDNS"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "YYYYYYYYEEEE34024932849034843YYYYYFFBJDSLKDLKNFNSLDJNFJLKSNLKDNS"
        cancelation_type = "Final"
        reason = "No puedo asistir ya que juega el Betis"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("Firma de la cita invalida", error.exception.message)

    def test_tipo_incorrecto(self):
        """El tipo es incorrecto"""
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_date.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex
        datos_cita = [{
            "_VaccinationAppointment__alg": "SHA-256",
            "_VaccinationAppointment__type": "DS",
            "_VaccinationAppointment__patient_sys_id": "72b72255619afeed8bd26861a2bc2caf",
            "_VaccinationAppointment__patient_id": "78924cb0-075a-4099-a3ee-f3b562e805b9",
            "_VaccinationAppointment__phone_number": "+34123456789",
            "_VaccinationAppointment__issued_at": 2646697600.0,
            "_VaccinationAppointment__appointment_date": 2646697600.0,
            "_VaccinationAppointment__date_signature": "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
        cancelation_type = "Hasbullah"
        reason = "No puedo asistir ya que juega el Betis"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("Tipo de cancelación erroneo", error.exception.message)

    def test_reason_incorrecta(self):
        """La razon no tiene el formato correcto"""

        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_date.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex
        datos_cita = [{
            "_VaccinationAppointment__alg": "SHA-256",
            "_VaccinationAppointment__type": "DS",
            "_VaccinationAppointment__patient_sys_id": "72b72255619afeed8bd26861a2bc2caf",
            "_VaccinationAppointment__patient_id": "78924cb0-075a-4099-a3ee-f3b562e805b9",
            "_VaccinationAppointment__phone_number": "+34123456789",
            "_VaccinationAppointment__issued_at": 2646697600.0,
            "_VaccinationAppointment__appointment_date": 2646697600.0,
            "_VaccinationAppointment__date_signature": "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
        cancelation_type = "Temporal"
        reason = "Esto es una razón para anular la cita demasiado larga que no sería aceptada por contener más caracteres de los permitidos según el programa. El máximo establecido por el enunciado es de 100"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("Longitud de la razon invalida", error.exception.message)

    def test_se_ha_administrado_previamente(self):
        """La vacuna ya se ha administrado"""
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_vaccine.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        administrated = [{"_VaccinationLog__date_signature": "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70",
                "_VaccinationLog__timestamp": 1646697600.0}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(administrated, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Temporal"
        reason = "Hola"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("La vacuna que se pretende anular ya se ha administrado", error.exception.message)

    def test_se_ha_cancelado_como_final_previamente(self):
        """La cita ya se ha cancelado completamente"""
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_vaccine.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Final"
        reason = "Hola"
        cancelado = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump(cancelado, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Final"
        reason = "Hola"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("La vacuna que se pretende anular ya había sido cancelada", error.exception.message)

    def test_no_existe_la_cita_en_el_archivo(self):
        """No se encuentra la cita"""
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_vaccine.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        ruta4 = JSON_FILES_PATH + "store_date.json"
        if os.path.isfile(ruta4):
            os.remove(ruta4)

        no_existe = [{"_VaccinationAppointment__alg": "SHA-256",
    "_VaccinationAppointment__type": "DS",
    "_VaccinationAppointment__patient_sys_id": "72b72255619afeed8bd26861a2bc2caf",
    "_VaccinationAppointment__patient_id": "78924cb0-075a-4099-a3ee-f3b562e805b9",
    "_VaccinationAppointment__phone_number": "+34123456789",
    "_VaccinationAppointment__issued_at": 2646697600.0,
    "_VaccinationAppointment__appointment_date": 2646697600.0,
    "_VaccinationAppointment__date_signature": "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]

        try:
            with open(ruta4, "w", encoding="utf-8", newline="") as file:
                json.dump(no_existe, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Final"
        reason = "Hola"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("La cita que se pretende cancelar no existe", error.exception.message)

    def test_se_modifica_el_tipo(self):
        """Se cancela completamente la cita"""
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_vaccine.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        ruta4 = JSON_FILES_PATH + "store_date.json"
        if os.path.isfile(ruta4):
            os.remove(ruta4)

        no_existe = [{"_VaccinationAppointment__alg": "SHA-256",
                      "_VaccinationAppointment__type": "DS",
                      "_VaccinationAppointment__patient_sys_id": "72b72255619afeed8bd26861a2bc2caf",
                      "_VaccinationAppointment__patient_id": "78924cb0-075a-4099-a3ee-f3b562e805b9",
                      "_VaccinationAppointment__phone_number": "+34123456789",
                      "_VaccinationAppointment__issued_at": 2646697600.0,
                      "_VaccinationAppointment__appointment_date": 2646697600.0,
                      "_VaccinationAppointment__date_signature": "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"}]

        try:
            with open(ruta4, "w", encoding="utf-8", newline="") as file:
                json.dump(no_existe, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Temporal"
        reason = "Hola"
        cancelado = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump(cancelado, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Final"
        reason = "Hola"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        my_manager = VaccineManager()
        res = my_manager.cancel_appointment(ruta)
        self.assertEqual(res, "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70")
        # Además, se comprueba si en el fichero de canceladas se ha sido modificado con éxito

        lectura_canceled = JsonParser(ruta3)
        lectura_canceled.load_json_content()
        contenido = lectura_canceled.json_content
        self.assertEqual(contenido, data_list)

    def test_se_anade_la_cita_a_las_canceladas(self):
        """Se cancela la cita"""
        ruta = JSON_FILES_TESTS_PATH + "todo_ok.json"
        ruta2 = JSON_FILES_PATH + "store_vaccine.json"
        if os.path.isfile(ruta2):
            os.remove(ruta2)

        ruta3 = JSON_FILES_PATH + "store_canceled.json"
        if os.path.isfile(ruta3):
            os.remove(ruta3)

        ruta4 = JSON_FILES_PATH + "store_date.json"
        if os.path.isfile(ruta4):
            os.remove(ruta4)

        no_existe = [{"_VaccinationAppointment__alg": "SHA-256",
                      "_VaccinationAppointment__type": "DS",
                      "_VaccinationAppointment__patient_sys_id": "72b72255619afeed8bd26861a2bc2caf",
                      "_VaccinationAppointment__patient_id": "78924cb0-075a-4099-a3ee-f3b562e805b9",
                      "_VaccinationAppointment__phone_number": "+34123456789",
                      "_VaccinationAppointment__issued_at": 2646697600.0,
                      "_VaccinationAppointment__appointment_date": 2646697600.0,
                      "_VaccinationAppointment__date_signature": "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"}]

        try:
            with open(ruta4, "w", encoding="utf-8", newline="") as file:
                json.dump(no_existe, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        try:
            with open(ruta3, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump([], file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        date_signature = "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70"
        cancelation_type = "Final"
        reason = "Hola"
        data_list = [{"date_signature": date_signature,
                      "cancelation_type": cancelation_type,
                      "reason": reason
                      }]
        try:
            with open(ruta, "w", encoding="utf-8", newline="") as file:
                json.dump(data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        my_manager = VaccineManager()
        res = my_manager.cancel_appointment(ruta)
        self.assertEqual(res, "2c8c5d3bd35ed637d8823344371ae9c64291bb9510001ee96016dc255eb74f70")
        # Además, se comprueba si en el fichero de canceladas se encuentra registrada la cita correctamente

        lectura_canceled = JsonParser(ruta3)
        lectura_canceled.load_json_content()
        contenido = lectura_canceled.json_content
        self.assertEqual(contenido, data_list)


if __name__ == '__main__':
    unittest.main()
