"""Module """
from uc3m_care.comprobacion.comprobacion import Comprobacion
from uc3m_care.data.vaccine_patient_register import VaccinePatientRegister
from uc3m_care.data.vaccination_appointment import VaccinationAppointment
from uc3m_care import JSON_FILES_PATH
from uc3m_care.cancelacion.cancelacion import Cancelacion


class VaccineManager:
    """Class for providing the methods for managing the vaccination process"""
    # pylint: disable=invalid-name
    class __VaccineManager:
        def __init__(self):
            pass
        # pylint: disable=too-many-arguments
        # pylint: disable=no-self-use
        def request_vaccination_id(self, patient_id,
                                   name_surname,
                                   registration_type,
                                   phone_number,
                                   age):
            """Register the patinent into the patients file"""
            my_patient = VaccinePatientRegister(patient_id,
                                                name_surname,
                                                registration_type,
                                                phone_number,
                                                age)
            my_patient.save_patient()
            return my_patient.patient_sys_id

        def get_vaccine_date(self, input_file, date="2030-12-01"):
            """Gets an appointment for a registered patient"""
            # Aqui obtenemos la cita para la ruta proporcionada
            my_sign = VaccinationAppointment.create_appointment_from_json_file(input_file, date)
            # save the date in store_date.json
            my_sign.save_appointment()
            return my_sign.date_signature

        def vaccine_patient(self, date_signature):
            """Register the vaccination of the patient"""
            appointment = VaccinationAppointment.get_appointment_from_date_signature(date_signature)

            return appointment.register_vaccination()

        def cancel_appointment(self, input_file):
            """Esta función cancela una cita si esta cumple los requisitos"""
            comprobacion = Comprobacion(input_file)

            ruta_cancelados = JSON_FILES_PATH + "store_canceled.json"
            cancelacion = Cancelacion()
            if comprobacion.cambio_temp_final:
                data_list, ruta = cancelacion.cambiar_tipo_cancelacion(comprobacion)
                cancelacion.escribir_cancelacion(data_list, ruta)
            else:
                cancelacion.escribir_cancelacion(comprobacion.datos, ruta_cancelados)
            return comprobacion.date_signature

    instance = None

    def __new__(cls):
        if not VaccineManager.instance:
            VaccineManager.instance = VaccineManager.__VaccineManager()
        return VaccineManager.instance

    def __getattr__(self, nombre):
        return getattr(self.instance, nombre)

    def __setattr__(self, nombre, valor):
        return setattr(self.instance, nombre, valor)
