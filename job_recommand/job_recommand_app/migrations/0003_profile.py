# Generated by Django 4.2 on 2023-04-07 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_recommand_app', '0002_alter_account_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.TextField()),
                ('role', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
    ]