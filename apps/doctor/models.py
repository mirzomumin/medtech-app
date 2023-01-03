from django.db import models

from helpers.models import BaseModel
from medical_record.models import MedicalRecord

# Create your models here.

class Doctor(BaseModel):
	'''Info about doctor'''

	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	specialization = models.CharField(max_length=128)

	def __str__(self):
		return f'{self.first_name} {self.last_name} - {self.specialization}'


class DoctorAppointment(BaseModel):
	'''Doctor appointment on a medical card'''

	# Relations
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,
		related_name='appointments')
	medical_record = models.ForeignKey(MedicalRecord,
		on_delete=models.CASCADE, related_name='appointments')

	def __str__(self):
		f'Doctor: {self.doctor.first_name} {self.doctor.last_name}\
		Patient: {self.medical_record.first_name} {self.medical_record.last_name}'