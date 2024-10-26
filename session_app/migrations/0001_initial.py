# Generated by Django 5.1.1 on 2024-10-26 06:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('name', models.CharField(max_length=100)),
                ('contact_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SessionHeaderImage',
            fields=[
                ('headerimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home_app.headerimage')),
            ],
            bases=('home_app.headerimage',),
        ),
        migrations.CreateModel(
            name='SessionSidebarNews',
            fields=[
                ('sidebarnews_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home_app.sidebarnews')),
            ],
            bases=('home_app.sidebarnews',),
        ),
        migrations.CreateModel(
            name='AvailableTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='available_times', to='session_app.availabledate')),
            ],
        ),
    ]
