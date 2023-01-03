from django.db import models

from helpers.models import BaseModel
from medical_record.models import MedicalRecord
from doctor.models import Doctor

# Create your models here.

class MedicalFormOne(BaseModel):
	'''Simple Example of Medical Form 01'''

	headache = models.BooleanField(null=True, blank=True)
	nicotine_or_alcohol = models.BooleanField(null=True, blank=True)
	sport = models.BooleanField(null=True, blank=True)
	temperature = models.PositiveSmallIntegerField()

	# Relations
	medical_record = models.ForeignKey(MedicalRecord,
		on_delete=models.CASCADE, related_name='forms_one')
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,
		related_name='forms_one')

	def __str__(self):
		return f'Medical Form One for\
		{self.medical_record.first_name} {self.medical_record.last_name}'


class MedicalFormTwo(BaseModel):
	'''Simple Example of Medical Form 02'''

	blood_pressure = models.PositiveSmallIntegerField()
	knee_pain = models.BooleanField(null=True, blank=True)
	last_physical_labor = models.DateField(null=True, blank=True)

	# Relations
	medical_record = models.ForeignKey(MedicalRecord,
		on_delete=models.CASCADE, related_name='forms_two')
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,
		related_name='forms_two')

	def __str__(self):
		return f'Medical Form Two for\
		{self.medical_record.first_name} {self.medical_record.last_name}'