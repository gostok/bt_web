# Generated by Django 5.1.1 on 2024-10-31 11:17

import home_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimage',
            name='image',
            field=models.ImageField(upload_to='carousel_images/', validators=[home_app.models.validate_image_blog_carousel]),
        ),
    ]