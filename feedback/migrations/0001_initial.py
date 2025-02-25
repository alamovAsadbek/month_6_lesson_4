# Generated by Django 5.1.1 on 2024-09-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('status', models.BooleanField(default=False)),
                ('user_firstname', models.CharField(max_length=200)),
                ('user_lastname', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
