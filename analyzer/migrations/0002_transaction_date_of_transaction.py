# Generated by Django 4.2.6 on 2023-10-26 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date_of_transaction',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
