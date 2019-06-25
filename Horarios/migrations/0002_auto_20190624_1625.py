# Generated by Django 2.1.7 on 2019-06-24 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Horarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=20)),
                ('h_inicio', models.TimeField()),
                ('h_fin', models.TimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='horario',
            name='nombre',
            field=models.CharField(default='Horario_de_clase', max_length=20),
        ),
        migrations.AddField(
            model_name='bloque',
            name='horario_asignado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Horarios.Horario'),
        ),
    ]
