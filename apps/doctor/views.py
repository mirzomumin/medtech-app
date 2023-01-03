from rest_framework.generics import CreateAPIView

from .serializers import CreateDoctorAppointmentSerializer
from .models import DoctorAppointment
# Create your views here.


class CreateDoctorAppointmentView(CreateAPIView):
	'''Create appointment on medical record'''

	serializer_class = CreateDoctorAppointmentSerializer
	queryset = DoctorAppointment.objects.all()