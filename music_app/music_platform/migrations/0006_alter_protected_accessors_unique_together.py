# Generated by Django 4.2.2 on 2023-06-16 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_platform', '0005_music_uploads_model_protected_accessors'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='protected_accessors',
            unique_together={('music_id', 'email')},
        ),
    ]