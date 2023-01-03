from rest_framework.generics import CreateAPIView

from .models import MedicalFormOne, MedicalFormTwo
from .serializers import (
	CreateMedicalFormOneSerializer,
	CreateMedicalFormTwoSerializer)
# Create your views here.


class CreateMedicalFormOneView(CreateAPIView):
	'''Create Medical Form 01'''

	serializer_class = CreateMedicalFormOneSerializer
	queryset = MedicalFormOne.objects.all()


class CreateMedicalFormTwoView(CreateAPIView):
	'''Create Medical Form 02'''

	serializer_class = CreateMedicalFormTwoSerializer
	queryset = MedicalFormTwo.objects.all()