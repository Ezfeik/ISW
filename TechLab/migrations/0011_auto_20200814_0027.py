# Generated by Django 3.0.4 on 2020-08-14 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TechLab', '0010_auto_20200814_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TechLab.Paciente'),
        ),
    ]
