# Generated by Django 3.0.7 on 2020-06-19 22:26

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='removed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor='is_removed', null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='removed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor='is_removed', null=True),
        ),
        migrations.AlterField(
            model_name='fileset',
            name='removed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, editable=False, monitor='is_removed', null=True),
        ),
    ]