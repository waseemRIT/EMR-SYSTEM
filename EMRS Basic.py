import csv
from datetime import datetime
import random
from typing import List

""" Electronic Medical Record (EMR) """


class Physician:
    """
    A Physician Class That Contains:
    ID --> integer
    Name --> string
    Speciality --> string
    """

    def __init__(self, id: int, name: str, specialty: str):
        self._id = id
        self._name = name
        self._specialty = specialty

    @property
    def id(self) -> int:
        """Return the physician's id number."""
        return self._id

    @property
    def name(self) -> str:
        """Return the physician's name."""
        return self._name

    @property
    def specialty(self) -> str:
        """Return the physician's speciality."""
        return self._specialty

    @id.setter
    def id(self, new_id: int):
        """Change the physician's id number."""
        self._id = new_id

    @name.setter
    def name(self, new_name: str):
        """Change the physician's name."""
        self._name = new_name

    @specialty.setter
    def specialty(self, new_specialty: str):
        """Change the physician's speciality."""
        self._specialty = new_specialty

    def __str__(self) -> str:
        """Return a string representation of the physician when the Physician object is printed."""
        return f"Physician: {self.name}\nSpecialty: {self.specialty}\n"

    def __repr__(self) -> str:
        """
        Return a string representation of the Physician object, including the values of all of its fields.
        """
        return f"ID: {self.id}\nName: {self.name}\nSpecialty: {self.specialty}\n"


class Patient:
    """
    A class representing a patient in an electronic medical record (EMR) system.
    """

    def __init__(self, emr_id: int = 0, name: str = "not specified", gender: str = "not specified",
                 phone_number: int = 0):
        """
        Initialize the fields of a new Patient object.

        Arguments:
        emr_id -- an integer representing the patient's EMR ID number (default is 0)
        name -- a string representing the patient's name (default is "not specified")
        gender -- a string representing the patient's gender (default is "not specified")
        phone_number -- an integer representing the patient's phone number (default is 0)
        """
        self.emr_id = emr_id
        self.name = name
        self.gender = gender
        self.phone_number = phone_number

    def __str__(self) -> str:
        """
        Return a string representation of the patient.
        """
        return f"Patient(id={self.emr_id}, name='{self.name}', gender='{self.gender}', phone_number='{self.phone_number}')"

    def __repr__(self) -> str:
        """
        Return a string representation of the Patient object, including the values of all of its fields.
        """
        return f"emr_id: {self.emr_id}\nname: {self.name}\ngender: {self.gender}\nphone number: {self.phone_number}\n"

    @property
    def emr_id(self) -> int:
        """
        Returns the emr_id of patient
        """
        return self.__emr_id

    @emr_id.setter
    def emr_id(self, emr_id: int):
        """
        Update the emr_id of patient
        """
        self.__emr_id = emr_id

    @property
    def name(self) -> str:
        """
        Returns the name of the patient
        """
        return self.__name

    @name.setter
    def name(self, name: str):
        """
        Update the name of patient
        """
        self.__name = name

    @property
    def gender(self) -> str:
        """
        Returns the gender of patient
        """
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        """
        Update the gender of patient
        """
        self.__gender = gender

    @property
    def phone_number(self) -> int:
        """
        Returns the phone_number of patient
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number: int):
        """
        Update the phone_number of patient
        """
        self.__phone_number = phone_number


# 3 - DONE
class Encounter:
    """
    A class representing an encounter between a patient and a physician in an electronic medical record (EMR) system.
    """

    def __init__(self, physician: Physician, patient: Patient, date: str, disease: str, medication: str):
        """
        Initialize the fields of a new Encounter object.

        Arguments:
        physician -- a Physician object representing the physician involved in the encounter
        patient -- a Patient object representing the patient involved in the encounter
        date -- a string representing the date of the encounter in the format "dd/mm/yy"
        disease -- a string representing the diagnosis made during the encounter
        medication -- a string representing the medication prescribed during the encounter
        """
        self._physician = physician
        self._patient = patient
        self._date = date
        self._disease = disease
        self._medication = medication

    @property
    def physician(self) -> Physician:
        """Return the physician involved in the encounter."""
        return self._physician

    @property
    def patient(self) -> Patient:
        """Return the patient involved in the encounter."""
        return self._patient

    @property
    def date(self) -> str:
        """Return the date of the encounter."""
        return self._date

    @property
    def disease(self) -> str:
        """Return the diagnosis made during the encounter."""
        return self._disease

    @property
    def medication(self) -> str:
        """Return the medication prescribed during the encounter."""
        return self._medication

    def __str__(self) -> str:
        """
        Return a string representation of the encounter, including the name of the patient and the physician. """
        return f"Encounter between {self.patient.name} and {self.physician.name}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Encounter object, including the values of all of its fields.
        """
        return (f"Encounter between {self.patient.name} and {self.physician.name}\n"
                f"Date: {self.date}\n"
                f"Disease: {self.disease}\n"
                f"Medication: {self.medication}\n")


def add_encounter(encounter, filename='encounter.csv'):
    """
    Add a new encounter to a CSV file.

    Arguments:
    encounter -- a tuple containing the information for the encounter
                 (physician, patient, date, disease, medication)
    filename -- the name of the CSV file to add the encounter to (default is 'encounter.csv')
    """
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(encounter)


def retrieve_physicians(filename):
    """
    Retrieve all physicians from a CSV file.

    Arguments:
    filename -- the name of the CSV file containing the physicians

    Returns:
    A list of tuples, where each tuple contains the attributes of a physician
    """
    with open(filename) as f:
        reader = csv.reader(f)
        physicians = [tuple(row) for row in reader]
    return physicians


def retrieve_patients(filename):
    """
    Retrieve all patients from a CSV file.

    Arguments:
    filename -- the name of the CSV file containing the patients

    Returns:
    A list of tuples, where each tuple contains the attributes of a patient
    """
    with open(filename) as f:
        reader = csv.reader(f)
        patients = [tuple(row) for row in reader]
    return patients


def process_physicians(physicians):
    physician_objects = []
    headers = physicians[0]
    for physician_data in physicians[1:]:
        id, name, speciality = physician_data
        physician = Physician(id, name, speciality)
        physician_objects.append(physician)
    return physician_objects


def process_patients(patient_data):
    patient_objects = []
    headers = patient_data[0]
    for i in range(1, len(patient_data)):
        emr_id, pname, gender, phone_num = patient_data[i]
        patient_objects.append(Patient(emr_id, pname, gender, phone_num))
    return patient_objects


def write_csv_header(fields, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(fields)


def write_encounters_to_csv(encounters: List[Encounter]):
    fieldnames = ["Physician", "Patient", "Date", "Disease", "Medication"]
    filename = "encounters.csv"
    write_csv_header(fieldnames, filename)
    with open(filename, "a") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for encounter in encounters:
            writer.writerow({
                "Physician": encounter.physician.name,
                "Patient": encounter.patient.name,
                "Date": encounter.date,
                "Disease": encounter.disease,
                "Medication": encounter.medication
            })


def main():
    # will store all the physicians here
    physicians = retrieve_physicians(r"physicians.csv")
    physician_objects = process_physicians(physicians)

    # will store all patients here
    patients = retrieve_patients(r"patients.csv")
    patient_objects = process_patients(patients)

    encounter_objects = []

    # Diseases List
    diseases = ["anxiety", "diabetes", "face rash", "high blood pressure", "high cholesterol"]

    # Medications List
    medications = ["Xanax", "Linagliptin", "Calamine", "Diuretics", "Atorvastatin"]

    # create a list of encounter with different dates, diseases, and medications
    for physician, patient in zip(physician_objects, patient_objects):
        # generate a random date
        date = datetime.strftime(datetime.now(), "%d/%m/%y")
        # generate a random disease from the list
        disease = random.choice(diseases)
        # generate a random medication from the list
        medication = random.choice(medications)

        encounter_objects.append(Encounter(physician, patient, date, disease, medication))

    # printing the patients
    print("Patients:-> \n")
    for patient in patient_objects:
        print(patient.__repr__())

    # to differentiate between patients and physicians
    print("#########################################################\n")

    print("Physicians:-> \n")
    for physician in physician_objects:
        print(physician.__repr__())

    # to differentiate between Encounters and the others
    print("#########################################################\n")

    # Printing the Encounters
    print("Encounters:->\n")
    for encounter in encounter_objects:
        print(encounter.__repr__())

    ''' To Add Encounters into the Encounters.csv File '''

    write_encounters_to_csv(encounter_objects)


if __name__ == '__main__':
    main()
