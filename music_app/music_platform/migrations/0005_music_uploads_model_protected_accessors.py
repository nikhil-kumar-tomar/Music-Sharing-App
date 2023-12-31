# Generated by Django 4.2.2 on 2023-06-15 21:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('music_platform', '0004_remove_protected_accessors_music_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='music_uploads_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('music_name', models.CharField(max_length=400)),
                ('music_file', models.FileField(upload_to='music/')),
                ('music_type', models.CharField(max_length=10)),
                ('owner_email', models.EmailField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='protected_accessors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300)),
                ('music_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_platform.music_uploads_model')),
            ],
        ),
    ]
