# Generated by Django 4.2.7 on 2023-11-12 13:14

import autoslug.fields
import dirtyfields.dirtyfields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import neighbour.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConnection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('connection_status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('DECLINED', 'Declined')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from=neighbour.models.get_slug, unique=True)),
                ('connected_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connected_user_connections', to=settings.AUTH_USER_MODEL)),
                ('current_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_user_connections', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(dirtyfields.dirtyfields.DirtyFieldsMixin, models.Model),
        ),
    ]
