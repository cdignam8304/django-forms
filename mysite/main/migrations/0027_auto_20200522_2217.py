# Generated by Django 2.2.12 on 2020-05-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20200522_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generic',
            name='date1',
            field=models.DateField(blank=True, default=None, verbose_name='date1'),
        ),
        migrations.AlterField(
            model_name='generic',
            name='date2',
            field=models.DateField(blank=True, default=None, verbose_name='date2'),
        ),
        migrations.AlterField(
            model_name='generic',
            name='date3',
            field=models.DateField(blank=True, default=None, verbose_name='date3'),
        ),
    ]