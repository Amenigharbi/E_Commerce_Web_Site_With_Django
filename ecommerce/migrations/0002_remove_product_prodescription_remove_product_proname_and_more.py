# Generated by Django 4.2.5 on 2023-10-02 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Prodescription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Proname',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proImag', models.ImageField(upload_to='proImages/%y/%m/%d', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.product', verbose_name='name of product ')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='ProDescription',
            field=models.TextField(default='text', verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='ProName',
            field=models.CharField(default='name', max_length=50, verbose_name='product name'),
        ),
    ]
