# Generated by Django 4.2.2 on 2023-08-20 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="Modalidad",
            field=models.IntegerField(
                choices=[
                    (0, "--SELECCIONE MODALIDAD--"),
                    (1, "TELETRABAJO"),
                    (1, "PRESENCIAL"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="Sede",
            field=models.IntegerField(
                choices=[
                    (0, "--SELECCIONE UNA SEDE--"),
                    (1, "Hospital del trabajador [HT]"),
                    (2, "Centro Medico [CEM]"),
                    (3, "ESACHS [Ramon Carnicer 151]"),
                    (4, "Rancagua 333"),
                    (5, "OTEC"),
                    (6, "ESE-CENTRO DE COMANDO [TERRENO]"),
                    (7, "Casa Central"),
                ],
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="TipoReporte",
            field=models.IntegerField(
                choices=[
                    (0, "--SELECCION DE REPORTE--"),
                    (1, "INCIDENCIA"),
                    (2, "REQUERIMIENTO"),
                ],
                null=True,
            ),
        ),
    ]
