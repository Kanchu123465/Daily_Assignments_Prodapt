# Generated by Django 3.2.6 on 2021-08-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor1',
            name='lastdonateddate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='donor1',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]