# Generated by Django 4.2.6 on 2023-10-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0002_alter_category_options_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
