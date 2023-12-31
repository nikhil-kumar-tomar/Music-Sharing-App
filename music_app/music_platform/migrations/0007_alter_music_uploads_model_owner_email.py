# Generated by Django 4.2.2 on 2023-06-16 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_platform', '0006_alter_protected_accessors_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music_uploads_model',
            name='owner_email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='email'),
        ),
    ]
