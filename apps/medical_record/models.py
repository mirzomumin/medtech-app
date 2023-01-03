from django.db import models
import datetime

from helpers.models import BaseModel

# Create your models here.

class MedicalRecord(BaseModel):
	'''Medical Record of patient'''

	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	birth_date = models.DateField()
	address = models.CharField(max_length=128)
	occupation = models.CharField(max_length=128)

	def __str__(self):
		return f'{self.first_name} {self.last_name} - {self.birth_date}'

	@property
	def age(self):
		today = datetime.date.today()
		delta = (today.year - self.birth_date.year -
			((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))
		return delta