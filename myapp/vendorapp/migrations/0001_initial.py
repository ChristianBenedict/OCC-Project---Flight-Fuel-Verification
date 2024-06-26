# Generated by Django 5.0.3 on 2024-06-07 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FuelAgentName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_agent_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FuelVendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Flight', models.CharField(max_length=50)),
                ('Dep', models.CharField(max_length=100)),
                ('Arr', models.CharField(max_length=100)),
                ('Reg', models.CharField(max_length=20)),
                ('Uplift_in_Lts', models.FloatField()),
                ('Invoice', models.CharField(max_length=100, unique=True)),
                ('Vendor', models.CharField(max_length=150)),
            ],
        ),
    ]