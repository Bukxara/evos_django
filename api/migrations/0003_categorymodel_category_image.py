# Generated by Django 4.1.7 on 2023-02-19 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_productmodel_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='category_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
