#EMR-SYSTEM

A simple Electronic Medical Record (EMR) application to keep track of all encounters between physicians and patients. One patient can have multiple encounters with different physicians. One physician can be involved in treatment for many patients.

##Description

This application is written in python and uses classes to represent physicians and patients. The Physician class contains properties for the physician's id number, name, and specialty. The Patient class contains properties for the patient's EMR ID, name, gender, and phone number.

The Physician class includes methods for getting and setting each property, as well as special methods __str__ and __repr__ that provide a more user-friendly string representation of the physician object when printed.

The Patient class also includes methods for getting and setting each property, as well as special methods __str__ and __repr__ that provide a more user-friendly string representation of the patient object when printed.

Additionally the Patient class have the property emr_id, name, gender and phone_number with their getter and setter methods.

##Usage

To use the EMR system, you can create an instance of a Physician or Patient class, set the properties, and then call the special methods to print out the object.

```py

# creating an instance of physician
dr_john = Physician(1, "John", "Surgeon")

# creating an instance of patient
patient_1 = Patient(1, "Alex", "male", 1234567890)

# get the physician id
print(dr_john.id) # 1

# get the patient name
print(patient_1.name) # Alex

# Print the physician and patient object
print(dr_john)
print(patient_1)
```
##Note
This is a simple EMR system designed for demonstration purpose, it does not provide any functionality related to patient-physician encounter management.
