""" Assignment 3  -  Electronic Medical Record (EMR) """


class Physician:
    """
    A Physician Class
    A physician has
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

    # Returns id
    def get_id(self):
        return self.__id

    # Returns name
    def get_name(self):
        return self.__name

    # Returns the speciality
    def get_speciality(self):
        return self.__specialty

    # Changes the id
    def set_id(self, new_id):
        self.__id = new_id

    # Changes the name
    def set_name(self, new_name):
        self.__name = new_name

    # Changes the speciality
    def set_specialty(self, new_speciality):
        self.__specialty = new_speciality

    ''' 1 c - DONE'''
    # Returns the Physician's name
    def __str__(self):
        return f"Physician {self.__name}"

    # Returns the Physicians specified attributes
    def __repr__(self):
        return f"name: {self.__name}\nid: {self.__id}\nspeciality: {self.__specialty}\n"


class Patient:
    """
    A Patient Class
    Includes
    emr_id --> integer -- IF = TO 0 THEN NONE
    name --> string
    gender --> string
    phone_number --> integer  -- IF = TO 0 THEN NONE
    """

    ''' 2 a - DONE'''
    # Defining the fields in slots
    __slots__ = ["__emr_id", "__name", "__gender", "__phone_number"]

    # Initializing the fields in the constructor
    def __init__(self, emr_id=0, name="not specified", gender="not specified",
                 phone_number=0):
        self.__gender = gender
        self.__phone_number = phone_number
        self.__name = name
        self.__emr_id = emr_id

    ''' 2 b - DONE'''
    # returns emr_id
    def get_emr_id(self):
        return self.__emr_id

    # Returns name
    def get_name(self):
        return self.__name

    # Returns gender
    def get_gender(self):
        return self.__gender

    # Returns Phone Number
    def get_phone_number(self):
        return self.__phone_number

    # Changes emr_id
    def set_emr_id(self, new_emr_id):
        self.__emr_id = new_emr_id

    # Changes name
    def set_name(self, new_name):
        self.__name = new_name

    # changes gender
    def set_gender(self, new_gender):
        self.__gender = new_gender

    # changes phone number
    def set_phone_number(self, new_phone_number):
        self.__phone_number = new_phone_number

    ''' 2 c - DONE'''

    # print's the patient's name
    def __str__(self):
        return f"patient {self.__name}"

    # print's the patients full details
    def __repr__(self):
        return f"emr_id{self.__emr_id}\nname: {self.__name}\ngender: {self.__gender}\nphone number: {self.__phone_number}\n "


class Encounter:
    """
    Used to record the encounters between patients and physicians.
    it takes:
    physician --> string
    patient --> string
    date  --> string dd/mm/yy
    disease --> string
    medication --> string
    """

    # Defining the fields in slots
    __slots__ = ["physician", "patient", "date", "disease", "medication"]

    # Initializing the fields in the constructor
    def __init__(self, physician, patient, date, disease, medication):
        self.medication = medication
        self.disease = disease
        self.date = date
        self.patient = patient
        self.physician = physician

    # returns physician name
    def get_physician(self):
        return self.physician

    def get_patient(self):
        return self.patient

    def get_date(self):
        return self.date

    def get_disease(self):
        return self.disease

    def get_medication(self):
        return self.medication


def main():
    # The Physicians
    physician1 = Physician(12, "Waseem", "Neurologists")
    physician2 = Physician(13, "Kassem", "Anesthesiology")
    physician3 = Physician(14, "Mazen", "Dermatology")

    # The Patients
    patient1 = Patient(1, "wael", "male", 971561053678)
    patient2 = Patient(2, "Rami", "male", 971561053693)
    patient3 = Patient(3, "Rama", "female", 971561053628)
    patient4 = Patient(4, "Jude", "female", 971561034678)
    patient5 = Patient(5, "Wakeel", "male", 971561053267)
    patiient6 = Patient(6, "Osama", "male", 971561053378)
    patient7 = Patient(7, "Afra", "female", 971526753678)
    patient8 = Patient(8, "Rashid", "male", 971561278678)
    patient9 = Patient(9, "Mustafa", "male", 971561028678)
    patient10 = Patient(10, "Osama", "male", 971518053678)

    # The Encounters
    encount1 = Encounter(physician1, patient7, "13/11/21", "anxiety", "Xanax")
    encount2 = Encounter(physician2, patient4, "14/08/21", "face rash", "Calamine")
    encount3 = Encounter(physician1, patient3, "11/04/21", "diabetes", "Linagliptin")
    encount4 = Encounter(physician3, patient1, "06/010/21", "high blood pressure", "Diuretics")
    encount5 = Encounter(physician2, patient9, "04/08/21", "high cholesterol", "Atorvastatin")

    # printing the patients
    print(patient1)
    print(patient2)
    print(patient3)
    print(patient4)
    print(patient5)
    print(patiient6)
    print(patient7)
    print(patient8)
    print(patient9)
    print(patient10)

    # to differentiate between patients and physicians
    print("#########################################################")

    # printing the Physicians
    print(physician1)
    print(physician2)
    print(physician3)


main()
