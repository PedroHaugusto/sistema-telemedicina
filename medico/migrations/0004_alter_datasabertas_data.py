# Generated by Django 5.0.4 on 2024-04-18 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0003_datasabertas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasabertas',
            name='data',
            field=models.DateTimeField(),
        ),
    ]
