from rest_framework import serializers
import datetime

from .models import MedicalFormOne, MedicalFormTwo


class CreateMedicalFormOneSerializer(serializers.ModelSerializer):
	'''Serializer for creating medical form 01'''

	class Meta:
		model = MedicalFormOne
		fields = ('id', 'headache', 'nicotine_or_alcohol', 'sport',
			'temperature', 'medical_record', 'doctor', 'created_at')

	def validate_temperature(self, value):
		'''Validate the value of patient temperature'''

		if value >= 34 and value <= 42:
			return value
		raise serializers.ValidationError('Temperature value is not valid.\
			It should be in range 34 and 42')

	def validate_medical_record(self, value):
		'''Validate the age of patient'''

		if value.age >= 18 and value.age <= 30:
			return value
		raise serializers.ValidationError('Patient\'s age is not in range 18 and 30.\
			It is invalid form for this patient!')


class CreateMedicalFormTwoSerializer(serializers.ModelSerializer):
	'''Serializer for creating medical form 02'''

	class Meta:
		model = MedicalFormTwo
		fields = ('id', 'blood_pressure', 'knee_pain', 'last_physical_labor',
			'medical_record', 'doctor', 'created_at')

	def validate_blood_pressure(self, value):
		'''Validate patient blood pressure'''

		if value >= 100 and value <= 200:
			return value
		raise serializers.ValidationError('Boold pressure value is not valid.\
			It should be in range 100 and 200')

	def validate_last_physical_labor(self, value):
		'''Validate the date of last active physical labor of patient'''

		if value is not None:
			if (datetime.date.today() - value) >= datetime.timedelta(days=0):
				return value
			raise serializers.ValidationError('Last active physical labor value is not valid.\
				It should be maximum today\'s date')

	def validate_medical_record(self, value):
		'''Validate the age of patient'''

		if value.age > 30:
			return value
		raise serializers.ValidationError('Patient is not over 30 age.\
			It is invalid form for this patient!')


class GetMedicalFormOneSerializer(serializers.ModelSerializer):
	'''Serializer to get the medical form 01'''

	class Meta:
		model = MedicalFormOne
		fields = ('headache', 'nicotine_or_alcohol', 'sport',
			'temperature', 'doctor', 'created_at')
		read_only_fields = fields


class GetMedicalFormTwoSerializer(serializers.ModelSerializer):
	'''Serializer to get the medical form 02'''

	class Meta:
		model = MedicalFormTwo
		fields = ('blood_pressure', 'knee_pain', 'last_physical_labor',
			'doctor', 'created_at')
		read_only_fields = fields