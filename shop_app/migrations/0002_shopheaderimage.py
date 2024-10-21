# Generated by Django 5.1.1 on 2024-10-21 10:32

import shop_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopHeaderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop_header_images/', validators=[shop_app.models.validate_image])),
            ],
        ),
    ]
