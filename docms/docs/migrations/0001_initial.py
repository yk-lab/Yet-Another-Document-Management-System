# Generated by Django 3.0.7 on 2020-06-17 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('removed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='is_removed')),
                ('title', models.CharField(db_index=True, max_length=512, verbose_name='title')),
                ('summary', models.TextField(blank=True, verbose_name='summary')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documents', to=settings.AUTH_USER_MODEL, verbose_name='registered by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=256, verbose_name='code')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fileset',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('removed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='is_removed')),
                ('name', models.CharField(db_index=True, max_length=256, verbose_name='name')),
                ('summary', models.TextField(blank=True, verbose_name='summary')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filesets', to='docs.Document', verbose_name='document')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='filesets', to=settings.AUTH_USER_MODEL, verbose_name='registered by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('removed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='is_removed')),
                ('file', models.FileField(editable=False, upload_to='', verbose_name='file')),
                ('filename', models.CharField(max_length=256, verbose_name='filename')),
                ('memo', models.TextField(blank=True, verbose_name='memo')),
                ('fileset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='docs.Fileset', verbose_name='file')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='registered by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(related_name='documents', to='docs.Tag', verbose_name='tags'),
        ),
    ]