# Generated by Django 4.2.1 on 2023-05-11 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_uz_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='otdelkadrovpps',
            name='user',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]