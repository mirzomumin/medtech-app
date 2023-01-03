from django.urls import path

from .views import CreateDoctorAppointmentView

urlpatterns = [
	path('appointments/create/', CreateDoctorAppointmentView.as_view(),
		name='appointment_create'),
]