# Generated by Django 4.1 on 2023-02-11 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MicroServiceApp', '0003_account_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='created_by',
        ),
    ]
