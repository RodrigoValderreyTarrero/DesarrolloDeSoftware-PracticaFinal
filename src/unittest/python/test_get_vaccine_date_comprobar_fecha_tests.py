import unittest
from uc3m_care import VaccineManager
from uc3m_care import VaccineManagementException
from uc3m_care import JSON_FILES_TESTS_PATH


class TestComprobarFecha(unittest.TestCase):
    """Se comprueba si la fecha introducida como parámetro es correcta"""
    def test_fecha_formato_erroneo(self):
        file_test = JSON_FILES_TESTS_PATH + "test_ok.json"
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, "hola")
        self.assertEqual(c_m.exception.message, "Formato de fecha incorrecto")

    def test_fecha_mes_erroneo(self):
        """El mes introducido es erroneo"""
        file_test = JSON_FILES_TESTS_PATH + "test_ok.json"
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, "2030-13-12")
        self.assertEqual(c_m.exception.message, "Mes no válido")

    def test_fecha_dia_erroneo(self):
        """El día es incorrecto"""
        file_test = JSON_FILES_TESTS_PATH + "test_ok.json"
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, "2030-12-33")
        self.assertEqual(c_m.exception.message, "Día no válido")

    def test_request_registration_anterior(self):
        """El programa no debe permitir conceder citas pasadas"""
        file_test = JSON_FILES_TESTS_PATH + "test_ok.json"
        my_manager = VaccineManager()
        with self.assertRaises(VaccineManagementException) as c_m:
            my_manager.get_vaccine_date(file_test, "1988-10-11")
        self.assertEqual(c_m.exception.message, "Fecha anterior a la actual")




if __name__ == '__main__':
    unittest.main()
