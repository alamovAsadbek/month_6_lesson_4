# Generated by Django 5.1.1 on 2024-09-26 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicemodel',
            options={'verbose_name': 'Service', 'verbose_name_plural': 'Services'},
        ),
    ]
