# Generated by Django 3.0.2 on 2020-01-15 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gibson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gibson',
            name='field_name',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
