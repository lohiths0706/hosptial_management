from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    special=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True)
    address=models.TextField()

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ManyToManyField(Patient)
    date=models.DateField()
    time=models.TimeField()

    def __str__(self):
        patient_names = ', '.join([str(patient) for patient in self.patient.all()])
        return f"Appointment - {self.doctor} - {self.patient}"
