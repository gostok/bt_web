# Generated by Django 5.1.1 on 2024-10-21 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_product_seller_productimage_product_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='contacts',
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_type', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=200)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='shop_app.seller')),
            ],
        ),
    ]
