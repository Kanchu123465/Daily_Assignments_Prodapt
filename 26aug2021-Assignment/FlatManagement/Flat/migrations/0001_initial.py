# Generated by Django 3.2.6 on 2021-08-26 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bno', models.IntegerField()),
                ('ownername', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('aadhar', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]