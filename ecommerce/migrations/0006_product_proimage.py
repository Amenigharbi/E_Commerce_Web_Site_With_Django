# Generated by Django 4.2.5 on 2023-10-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0005_product_prodbrand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='proImage',
            field=models.ImageField(blank=True, null=True, upload_to='proImages/%y/%m/%d', verbose_name='image'),
        ),
    ]
