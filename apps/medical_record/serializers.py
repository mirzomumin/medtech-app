from rest_framework import serializers

from .models import MedicalRecord
from medical_form.serializers import (
	GetMedicalFormOneSerializer,
	GetMedicalFormTwoSerializer)


class ListMedicalRecordSerializer(serializers.ModelSerializer):
	'''Serializer for list of medical records'''

	class Meta:
		model = MedicalRecord
		fields = ('id', 'first_name', 'last_name', 'birth_date')


class DetailMedicalRecordSerializer(serializers.ModelSerializer):
	'''Serializer for single medical record'''

	forms_one = GetMedicalFormOneSerializer(many=True, read_only=True)
	forms_two = GetMedicalFormTwoSerializer(many=True, read_only=True)
	class Meta:
		model = MedicalRecord
		fields = ('id', 'first_name', 'last_name', 'birth_date',
			'address', 'occupation', 'forms_one', 'forms_two')
		read_only_fields = fields