# Generated by Django 3.2.6 on 2021-08-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donors',
            name='lastblddonate',
            field=models.CharField(default='', max_length=50),
        ),
    ]