# Generated by Django 3.2.3 on 2021-07-05 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GroundZero', '0002_auto_20210703_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='proveedores'),
        ),
    ]
