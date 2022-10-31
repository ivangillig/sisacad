# Generated by Django 4.1.2 on 2022-10-28 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0008_permission_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_name', models.CharField(max_length=40, unique=True, verbose_name='Título')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de ingreso')),
            ],
            options={
                'verbose_name': 'Título',
                'verbose_name_plural': 'Títulos',
            },
        ),
        migrations.AlterField(
            model_name='license',
            name='license_type',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Tipo de licencia'),
        ),
        migrations.CreateModel(
            name='Teacher_Degree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='documentos/titulos', verbose_name='Foto/Escaneo de Título')),
                ('graduated_date', models.DateField(blank=True, null=True, verbose_name='Fecha de graduación')),
                ('institution', models.CharField(blank=True, max_length=30, null=True, verbose_name='Otorgado por')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.degree', verbose_name='Título')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.teacher', verbose_name='Docente')),
            ],
            options={
                'verbose_name': 'Docente_Titulo',
                'verbose_name_plural': 'Docentes_Titulos',
            },
        ),
    ]