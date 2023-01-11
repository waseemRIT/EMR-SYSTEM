# EMR-SYSTEM

An Electronic Medical Record (EMR) application to keep track of encounters between physicians and patients. One patient can have multiple encounters with different physicians, and one physician can be involved in treatment for many patients.

## Description

This application is written in python and uses classes to represent physicians and patients. The Physician class contains properties for the physician's id number, name, and specialty. The Patient class contains properties for the patient's EMR ID, name, gender, and phone number.

In addition to the management of the physicians and patients record, this application also provides functionality related to the encounter management. Where the encounters can be recorded and later can be retrieved based on patient or physician.

The Physician class includes methods for getting and setting each property, as well as special methods __str__ and __repr__ that provide a more user-friendly string representation of the physician object when printed.

The Patient class also includes methods for getting and setting each property, as well as special methods __str__ and __repr__ that provide a more user-friendly string representation of the patient object when printed.

Additionally, the application provides a Encounter class which will hold the encounter details like date, diagnosis, medication prescribed and the physician and patient involved.

## Usage

To use the EMR system, you can create instances of the Physician, Patient, and Encounter classes, set the properties, and then call the special methods to print out the objects.

```py
# creating an instance of physician
dr_john = Physician(1, "John", "Surgeon")

# creating an instance of patient
patient_1 = Patient(1, "Alex", "male", 1234567890)

# creating an instance of encounter
encounter_1 = Encounter(patient_1, dr_john, "12/12/2022", "Fever", "Paracetamol")

# get the physician id
print(dr_john.id) # 1

# get the patient name
print(patient_1.name) # Alex

# Print the physician and patient object
print(dr_john)
print(patient_1)

# Print the encounter object
print(encounter_1)
```
## Note
This is a simple EMR system designed for demonstration purpose, it does not provide any advanced functionality related to patient-physician encounter management.
