# Generated by Django 3.0.4 on 2020-08-14 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TechLab', '0011_auto_20200814_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='paciente',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='TechLab.Paciente'),
        ),
    ]