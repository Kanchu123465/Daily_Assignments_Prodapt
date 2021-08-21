# Generated by Django 3.2.6 on 2021-08-20 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('pincode', models.IntegerField(default=False)),
                ('mobile_no', models.BigIntegerField(default=False)),
                ('last_donated_date', models.DateField(default=False)),
            ],
        ),
    ]