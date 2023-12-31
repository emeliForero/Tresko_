# Generated by Django 4.2.4 on 2023-08-14 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='userprofile')),
                ('firm', models.ImageField(blank=True, upload_to='firm')),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('identification', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=200, null=True)),
                ('role', models.CharField(choices=[('Terapeuta', 'Terapeuta'), ('Psicólogo', 'Psicólogo'), ('Nutricionista', 'Nutricionists'), ('Recepcionista', 'Recepcionista'), ('Coordinacion', 'Coordinacion'), ('Gerente', 'Gerente')], max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Profile')),
            ],
        ),
    ]
