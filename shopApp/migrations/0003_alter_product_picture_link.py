# Generated by Django 4.0.2 on 2022-02-28 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopApp', '0002_remove_product_picture_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture_link',
            field=models.URLField(default=''),
        ),
    ]
