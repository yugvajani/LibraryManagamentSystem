# Generated by Django 3.0.2 on 2020-10-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fine', '0002_fine_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fine',
            name='date_paid',
            field=models.DateField(null=True),
        ),
    ]