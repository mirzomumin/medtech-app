from rest_framework import serializers

from .models import DoctorAppointment


class CreateDoctorAppointmentSerializer(serializers.ModelSerializer):
	'''Serializer for creating doctor appointment'''

	class Meta:
		model = DoctorAppointment
		fields = '__all__'

	def validate_medical_record(self, value):
		'''Validate patient age'''

		if value.age > 18:
			return value
		raise serializers.ValidationError('Patient is under the age of 18.\
			You can\'t accept the patient')