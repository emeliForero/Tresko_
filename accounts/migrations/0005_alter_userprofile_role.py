# Generated by Django 4.2.4 on 2023-09-10 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('Terapeuta', 'Terapeuta'), ('Psicólogo', 'Psicólogo'), ('Nutricionista', 'Nutricionista'), ('Recepcionista', 'Recepcionista'), ('Coordinacion', 'Coordinacion'), ('Gerente', 'Gerente')], max_length=200, null=True),
        ),
    ]
