# Generated by Django 5.0.1 on 2024-01-22 12:50

import events.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=events.models.event_image_path)),
                ('date', models.DateField(blank=True, null=True)),
                ('organizations', models.ManyToManyField(to='organizations.organization')),
            ],
        ),
    ]
