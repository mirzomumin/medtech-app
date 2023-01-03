from django.urls import path

from .views import CreateMedicalFormOneView, CreateMedicalFormTwoView


urlpatterns = [
	path('one/create/', CreateMedicalFormOneView.as_view(), name='create_form_one'),
	path('two/create/', CreateMedicalFormTwoView.as_view(), name='create_form_two'),
]