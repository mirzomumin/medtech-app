from django.contrib import admin

from .models import MedicalRecord
# Register your models here.


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'birth_date', 'occupation')