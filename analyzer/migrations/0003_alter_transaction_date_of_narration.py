# Generated by Django 4.2.6 on 2023-10-26 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('analyzer', '0002_transaction_date_of_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_of_narration',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
