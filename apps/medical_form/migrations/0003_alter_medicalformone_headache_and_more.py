# Generated by Django 4.1.5 on 2023-01-03 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_form', '0002_medicalformone_doctor_medicalformtwo_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalformone',
            name='headache',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalformone',
            name='nicotine_or_alcohol',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalformone',
            name='sport',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalformtwo',
            name='knee_pain',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalformtwo',
            name='last_physical_labor',
            field=models.DateField(blank=True, null=True),
        ),
    ]
