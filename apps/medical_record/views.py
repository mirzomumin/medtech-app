from rest_framework.generics import get_object_or_404, ListAPIView, RetrieveAPIView

from .models import MedicalRecord
from .serializers import (
	ListMedicalRecordSerializer,
	DetailMedicalRecordSerializer)



class ListMedicalRecordView(ListAPIView):
	'''Get medical record list'''

	serializer_class = ListMedicalRecordSerializer
	queryset = MedicalRecord.objects.all()


class DetailMedicalRecordView(RetrieveAPIView):
	'''Get detail info of medical record'''

	serializer_class = DetailMedicalRecordSerializer
	queryset = MedicalRecord.objects.all()