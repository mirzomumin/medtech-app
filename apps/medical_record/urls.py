from django.urls import path

from .views import *


urlpatterns = [
	path('', ListMedicalRecordView.as_view(), name='medical_records'),
	path('<int:pk>/', DetailMedicalRecordView.as_view(),
		name='medical_record'),
]