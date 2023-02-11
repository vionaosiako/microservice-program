# Generated by Django 4.1 on 2023-02-11 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('othername', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('national_id', models.IntegerField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Account_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Number', models.TextField()),
                ('Account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroServiceApp.account')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MicroServiceApp.customer')),
            ],
        ),
    ]
