# Generated by Django 3.0.5 on 2020-04-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20200418_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientinfo',
            name='Computation',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]