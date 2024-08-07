# Generated by Django 5.0.6 on 2024-08-07 15:21

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('waiting', 'Waiting'), ('active', 'Active'), ('completed', 'Completed')], default='waiting', max_length=10)),
                ('max_participants', models.PositiveIntegerField()),
                ('max_duration', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_games', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(related_name='participated_games', to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='mcqs.mcqs')),
            ],
        ),
    ]
