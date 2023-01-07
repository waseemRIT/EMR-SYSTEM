import csv

""" Electronic Medical Record (EMR) """


class Physician:
    """
    A Physician Class That Contains:
    ID --> integer
    Name --> string
    Speciality --> string
    """

    ''' 1  a - DONE '''
    # Defining the fields in slots
    __slots__ = ["__id", "__name", "__specialty"]

    # Initializing the fields in the constructor
    def __init__(self, id, name, specialty):
        self.__id = id
        self.__name = name
        self.__specialty = specialty

    ''' 1 b - DONE '''

    # Returns Physician's id number
    def get_id(self):
        return self.__id

    # Returns Physician's name
    def get_name(self):
        return self.__name

    # Returns the Physician's speciality
    def get_speciality(self):
        return self.__specialty

    # Changes the Physician's id number
    def set_id(self, new_id):
        self.__id = new_id

    # Changes the Physician's name
    def set_name(self, new_name):
        self.__name = new_name

    # Changes the Physician's speciality
    def set_specialty(self, new_speciality):
        self.__specialty = new_speciality

    ''' 1 c - DONE'''

    # Returns the Physician's name when Physician Object is pronted
    def __str__(self):
        return f"Physician: {self.__name}\nspeciality: {self.__specialty}\n"

    # Returns the Physician's specified attributes
    def __repr__(self):
        return f"name: {self.__name}\nid: {self.__id}\nspeciality: {self.__specialty}\n"


class Patient:
    """
    A class representing a patient in an electronic medical record (EMR) system.
    """

    # Define the fields that the class will store
    __slots__ = ["__emr_id", "__name", "__gender", "__phone_number"]

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
        self.__gender = gender
        self.__phone_number = phone_number
        self.__name = name
        self.__emr_id = emr_id

    def get_emr_id(self) -> int:
        """Return the patient's EMR ID number."""
        return self.__emr_id

    def get_name(self) -> str:
        """Return the patient's name."""
        return self.__name

    def get_gender(self) -> str:
        """Return the patient's gender."""
        return self.__gender

    def get_phone_number(self) -> int:
        """Return the patient's phone number."""
        return self.__phone_number

    def set_emr_id(self, new_emr_id: int):
        """Change the patient's EMR ID number."""
        self.__emr_id = new_emr_id

    def set_name(self, new_name: str):
        """Change the patient's name."""
        self.__name = new_name

    def set_gender(self, new_gender: str):
        """Change the patient's gender."""
        self.__gender = new_gender

    def set_phone_number(self, new_phone_number: int):
        """Change the patient's phone number."""
        self.__phone_number = new_phone_number

    def __str__(self) -> str:
        """Return a string representation of the patient's name when the Patient object is printed."""
        return f"patient: {self.__name}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Patient object, including the values of all of its fields.
        """
        return f"emr_id: {self.__emr_id}\nname: {self.__name}\ngender: {self.__gender}\nphone number: {self.__phone_number}\n"


# 3 - DONE
class Encounter:
    """
    A class representing an encounter between a patient and a physician in an electronic medical record (EMR) system.
    """

    # Define the fields that the class will store
    __slots__ = ["__physician", "__patient", "__date", "__disease", "__medication"]

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
        self.__physician = physician
        self.__patient = patient
        self.__date = date
        self.__disease = disease
        self.__medication = medication

    def get_physician(self) -> str:
        """Return the name of the physician involved in the encounter."""
        return self.__physician.get_name()

    def get_patient(self) -> str:
        """Return the name of the patient involved in the encounter."""
        return self.__patient.get_name()

    def get_date(self) -> str:
        """Return the date of the encounter."""
        return self.__date

    def get_disease(self) -> str:
        """Return the diagnosis made during the encounter."""
        return self.__disease

    def get_medication(self) -> str:
        """Return the medication prescribed during the encounter."""
        return self.__medication

    def __str__(self) -> str:
        """
        Return a string representation of the patient's name and the physician's name when the Encounter object is printed.
        """
        return f"{self.__physician}\n{self.__patient}"

    def __repr__(self) -> str:
        """
        Return a string representation of the Encounter object, including the values of all of its fields.
        """
        return (f"physician: {self.__physician}\n"
                f"patient: {self.__patient}\n"
                f"date: {self.__date}\n"
                f"disease: {self.__disease}\n"
                f"medication: {self.__medication}\n")


# Used to add the Encounters in a CSV File
def add_encounter_csv(physician, patient, date, disease, medication):
    with open("encounter.csv", "a", newline="") as encounter:
        # A Tuple of my fields to add
        fields = (physician, patient, date, disease, medication)
        writer = csv.writer(encounter)
        writer.writerow(fields)


# Returns the Physician's attributes from a Physicians csv File
def physician_retriever(csv_file):
    all_physicians = []
    with open(csv_file) as physicians:
        physicians = csv.reader(physicians)
        for attributes in physicians:
            all_physicians.append(attributes)

    return all_physicians


# Returns the Patient's attributes from a Patients csv File
def patients_retriever(csv_file):
    all_patients = []
    with open(csv_file) as patient:
        patients = csv.reader(patient)
        for attributes in patients:
            all_patients.append(attributes)

    return all_patients


def main():
    # will store all the physicians here
    physicians = physician_retriever(r"physicians.csv")

    # the attributes of all physicians
    headers, physician1_atr, physician2_atr, physician3_atr = physicians

    # the attributes of each physicians separated
    id1, name1, speciality1, _ = physician1_atr  # physician 1 attributes
    id2, name2, speciality2, _ = physician2_atr  # physician 2 attributes
    id3, name3, speciality3, _ = physician3_atr  # physician 3 attributes

    # Defining The Physicians
    physician1 = Physician(id1, name1, speciality1)
    physician2 = Physician(id2, name2, speciality2)
    physician3 = Physician(id3, name3, speciality3)

    # will store all patients here
    patients = patients_retriever(r"patients.csv")

    # The attributes of all patients
    headers, patient1, patient2, patient3, patient4, patient5, \
    patient6, patient7, patient8, patient9, patient10 = patients

    # the attributes of each physicians separated

    emr_id1, pname1, gender1, phone_num1 = patient1  # Patient 1 attributes
    emr_id2, pname2, gender2, phone_num2 = patient2  # Patient 2 attributes
    emr_id3, pname3, gender3, phone_num3 = patient3  # Patient 3 attributes
    emr_id4, pname4, gender4, phone_num4 = patient4  # Patient 4 attributes
    emr_id5, pname5, gender5, phone_num5 = patient5  # Patient 5 attributes
    emr_id6, pname6, gender6, phone_num6 = patient6  # Patient 6 attributes
    emr_id7, pname7, gender7, phone_num7 = patient7  # Patient 7 attributes
    emr_id8, pname8, gender8, phone_num8 = patient8  # Patient 8 attributes
    emr_id9, pname9, gender9, phone_num9 = patient9  # Patient 9 attributes
    emr_id10, pname10, gender10, phone_num10 = patient10  # Patient 10 attributes

    # The Patients Objects Creation
    patient1 = Patient(emr_id1, pname1, gender1, phone_num1)
    patient2 = Patient(emr_id2, pname2, gender2, phone_num2)
    patient3 = Patient(emr_id3, pname3, gender3, phone_num3)
    patient4 = Patient(emr_id4, pname4, gender4, phone_num4)
    patient5 = Patient(emr_id5, pname5, gender5, phone_num5)
    patient6 = Patient(emr_id6, pname6, gender6, phone_num6)
    patient7 = Patient(emr_id7, pname7, gender7, phone_num7)
    patient8 = Patient(emr_id8, pname8, gender8, phone_num8)
    patient9 = Patient(emr_id9, pname9, gender9, phone_num9)
    patient10 = Patient(emr_id10, pname10, gender10, phone_num10)

    # The Encounters Objects Creation
    encounter1 = Encounter(physician1, patient7, "13/11/21", "anxiety", "Xanax")
    encounter2 = Encounter(physician2, patient4, "14/08/21", "face rash", "Calamine")
    encounter3 = Encounter(physician1, patient3, "11/04/21", "diabetes", "Linagliptin")
    encounter4 = Encounter(physician3, patient1, "06/010/21", "high blood pressure", "Diuretics")
    encounter5 = Encounter(physician2, patient9, "04/08/21", "high cholesterol", "Atorvastatin")

    # printing the patients

    print("Patients:-> \n")

    print(patient1)
    print(patient2)
    print(patient3)
    print(patient4)
    print(patient5)
    print(patient6)
    print(patient7)
    print(patient8)
    print(patient9)
    print(patient10)

    # to differentiate between patients and physicians
    print("#########################################################\n")

    print("Physicians:-> \n")

    # printing the Physicians
    print(physician1)
    print(physician2)
    print(physician3)

    # to differentiate between Encounters and the others
    print("#########################################################\n")

    print("Encounters:->\n")

    # Printing the Encounters
    print(encounter1, "\n")
    print(encounter2, "\n")
    print(encounter3, "\n")
    print(encounter4, "\n")
    print(encounter5)

    ''' To Add Encounters into the Encounters.csv File '''

    # I used this to add the headers, since I am appending in the function, so this will help in not rewriting the
    # headers every time the function is called
    with open("encounter.csv", "a", newline="") as encounter:
        # Tuple of headers
        headers = ("Physician", "Patient", "Date", "Disease", "Medication")
        writer = csv.writer(encounter)
        writer.writerow(headers)

    # Adds Encounter 1
    add_encounter_csv(encounter1.get_physician(), encounter1.get_patient(), encounter1.get_date(),
                      encounter1.get_disease(), encounter1.get_medication())

    # Adds Encounter 2
    add_encounter_csv(encounter2.get_physician(), encounter2.get_patient(), encounter2.get_date(),
                      encounter2.get_disease(), encounter2.get_medication())

    # Adds Encounter 3
    add_encounter_csv(encounter3.get_physician(), encounter3.get_patient(), encounter3.get_date(),
                      encounter3.get_disease(), encounter3.get_medication())

    # Adds Encounter 4
    add_encounter_csv(encounter4.get_physician(), encounter4.get_patient(), encounter4.get_date(),
                      encounter4.get_disease(), encounter4.get_medication())

    # Adds Encounter 5
    add_encounter_csv(encounter5.get_physician(), encounter5.get_patient(), encounter5.get_date(),
                      encounter5.get_disease(), encounter5.get_medication())


main()
