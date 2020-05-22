# Generated by Django 2.2.12 on 2020-05-22 19:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20200522_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_type', models.CharField(max_length=200, verbose_name='data type')),
                ('string1', models.CharField(max_length=200, verbose_name='string1')),
                ('string2', models.CharField(max_length=200, verbose_name='string2')),
                ('string3', models.CharField(max_length=200, verbose_name='string3')),
                ('string4', models.CharField(max_length=200, verbose_name='string4')),
                ('string5', models.CharField(max_length=200, verbose_name='string5')),
                ('date1', models.DateField(default=django.utils.timezone.now, verbose_name='date1')),
                ('date2', models.DateField(default=django.utils.timezone.now, verbose_name='date2')),
                ('date3', models.DateField(default=django.utils.timezone.now, verbose_name='date3')),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('ACCEPTED', 'Accepted'), ('REJECTED', 'Rejected'), ('DEFERRED', 'Deferred'), ('ESCALATED', 'Escalated')], default='OPEN', max_length=10, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
                'verbose_name_plural': 'Generic Datasets',
            },
        ),
    ]
