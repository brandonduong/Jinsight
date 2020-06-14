# Generated by Django 3.0.7 on 2020-06-13 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expiration_list', '0006_item_days_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='expirationlist',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expirationlist', to=settings.AUTH_USER_MODEL),
        ),
    ]
