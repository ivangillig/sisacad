# Generated by Django 4.1.2 on 2022-10-27 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.person')),
                ('cuil', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado')),
                ('seniority_date', models.DateField(blank=True, null=True, verbose_name='Fecha de antiguedad')),
                ('seniority_qty', models.IntegerField(blank=True, null=True, verbose_name='Antiguedd reconocida')),
                ('statistics', models.CharField(choices=[('En actividad', 'En actividad'), ('Tareas pasivas', 'Tareas pasivas'), ('Docentes afectados al JIF pero de otra POF', 'Docentes afectados al JIF pero de otra POF'), ('Docentes del JIF afectados a otro establecimiento', 'Docentes del JIF afectados a otro establecimiento'), ('Sin subvención', 'Sin subvención'), ('Baja', 'Baja'), ('Fuera de actividad', 'InaFuera de actividadctivo'), ('A.T. / Integrador', 'A.T. / Integrador'), ('Par pedagógico / Dep. de dirección privada', 'Par pedagógico / Dep. de dirección privada')], default='En actividad', max_length=50, verbose_name='Estadística')),
            ],
            options={
                'verbose_name': 'Docente',
                'verbose_name_plural': 'Docentes',
            },
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Teacher_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.documents', verbose_name='Documentación')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.teacher', verbose_name='Docente')),
            ],
            options={
                'verbose_name': 'Docente_Documento',
                'verbose_name_plural': 'Docentes_Documentos',
            },
        ),
    ]
