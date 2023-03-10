# Generated by Django 4.1.5 on 2023-01-03 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birth_date', models.DateField()),
                ('address', models.CharField(max_length=128)),
                ('occupation', models.CharField(max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
