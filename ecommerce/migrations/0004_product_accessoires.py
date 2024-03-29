# Generated by Django 4.2.5 on 2023-10-02 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_rename_prodescription_product_prodescription_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Accessoires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AccProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessoires_product', to='ecommerce.product')),
                ('PlanAcc', models.ManyToManyField(related_name='accessoires_product_plan', to='ecommerce.product')),
            ],
            options={
                'verbose_name': 'product accessoires',
                'verbose_name_plural': 'product accessoires',
            },
        ),
    ]
