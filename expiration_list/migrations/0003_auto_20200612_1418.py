# Generated by Django 3.0.7 on 2020-06-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_list', '0002_auto_20200611_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='good',
            field=models.CharField(max_length=50),
        ),
    ]
