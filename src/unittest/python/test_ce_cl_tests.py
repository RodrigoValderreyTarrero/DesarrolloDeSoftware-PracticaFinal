import unittest
import os
import json
from uc3m_care import JSON_FILES_PATH, JSON_FILES_TESTS_PATH
from uc3m_care import VaccineManagementException
from uc3m_care import VaccineManager


class TestCECL(unittest.TestCase):
    """Clase creada para evaluar la función cancel appointment"""

    def test_todo_ok(self):
        """En este test, todos los valores introducidos son correctos y
        el tipo de cancelación es Temporal"""
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
            "_VaccinationAppointment__date_signature": "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
        cancelation_type = "Temporal"
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
        firma = my_manager.cancel_appointment(ruta)
        self.assertEqual(firma, "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b")

    def test_date_signature_no_hex(self):
        """En este test se evalua el caso en el que el código que debería ser hexadecimal
        (firma de la cita) no lo es """

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

    def test_date_signature_40_hex(self):
        """Este test evalua el caso en el que el hexadecimal sea de 40 caracteres
        (menos de 64)"""
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
            "_VaccinationAppointment__date_signature": "aaaaaabaaafaaa2aaa7aaaaaaa3aaaaaaaa6aaaa"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "aaaaaabaaafaaa2aaa7aaaaaaa3aaaaaaaa6aaaa"
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

    def test_date_signature_70_hex(self):
        """Este test evalua el caso en el que el hexadecimal sea de 70 caracteres
        (menas de 64)"""
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
            "_VaccinationAppointment__date_signature": "aaaaaabaaafaaa2aaa7aaaaaaa3aaaaaaaa6aaaaaaaaaaaaaaddddddddddcccccccccc"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "aaaaaabaaafaaa2aaa7aaaaaaa3aaaaaaaa6aaaaaaaaaaaaaaddddddddddcccccccccc"
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

    def test_date_signature_63_hex(self):
        """Este test evalua el caso en el que el hexadecimal sea de 63 caracteres
        (Caso límite con menos de 64)"""
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
            "_VaccinationAppointment__date_signature": "AA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "AA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
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

    def test_date_signature_65_hex(self):
        """Este test evalua el caso en el que el hexadecimal sea de 65 caracteres
                (Caso límite con mas de 64)"""
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
            "_VaccinationAppointment__date_signature": "AAAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "AAAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
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

    def test_cancelation_final(self):
        """Se trata de un test válido (como el primero de todos) pero en el que la entrada del
        tipo de cancelación es Final. Asi se testea que el programa funcione bien también en este
        caso"""
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
            "_VaccinationAppointment__date_signature": "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"}]
        try:
            with open(ruta2, "w", encoding="utf-8", newline="") as file:
                json.dump(datos_cita, file, indent=2)
        except FileNotFoundError as ex:
            raise VaccineManagementException("Wrong file or file path") from ex

        # Se crea el json que recibe la función cancel_appointment
        date_signature = "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b"
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
        firma = my_manager.cancel_appointment(ruta)
        self.assertEqual(firma, "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b")

    def test_cancelation_otro(self):
        """En este test el tipo de cancelación no es ni Temporal ni Final"""
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

    def test_reason_0_caracter(self):
        """En este test la razón para cancelar la cita es de longitud 0.
        En consecuencia debe ser denegada."""
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
        reason = ""
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

    def test_reason_189_caracter(self):
        """La razon se sobrepasa y por tanto es invalido. (189 caracteres)."""
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

    def test_reason_2_caracter(self):
        """En esta ocasión, la razon es un caso límite (2 caracteres).
        Debería ser permitido ya que es el último valor aceptado"""
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
        reason = "No"
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
        firma = my_manager.cancel_appointment(ruta)
        self.assertEqual(firma, "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b")

    def test_reason_1_caracter(self):
        """El test debe devolver un error. Se trata de un caso límite que no se acepta (1 caracter)
        para la razón"""
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
        reason = "E"
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

    def test_reason_100_caracter(self):
        """Se debería aceptar puesto que es el caso límite aceptado (el más alto posible)"""
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
        reason = "Esta razon tiene que contener exactamente 100 caracteres ni uno mas ni uno menos. Así se comprueba e"
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
        firma = my_manager.cancel_appointment(ruta)
        self.assertEqual(firma, "AAA0953d112ab693b83d1ced965fcc670b558235361b9d1bd62536769a1efa3b")

    def test_reason_101_caracter(self):
        """El test debe devolver un error. Se trata de un caso límite que no se acepta (101 caracter)
        para la razón"""
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
        reason = "Esta razon tiene que contener exactamente 100 caracteres ni uno mas ni uno menos. Así se comprueba eo"
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

    def test_invalid_json(self):
        """Test invalido"""
        ruta = JSON_FILES_TESTS_PATH + "no_existe.json"
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("File is not found", error.exception.message)

    def test_invalid_format(self):
        """Test invalido"""
        ruta = JSON_FILES_TESTS_PATH + "test_formato_incorrecto.json"
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as error:
            my_manager.cancel_appointment(ruta)
        self.assertEqual("JSON Decode Error - Wrong JSON Format", error.exception.message)


if __name__ == '__main__':
    unittest.main()
