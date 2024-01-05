# Generated by Django 4.2.5 on 2023-10-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BDName', models.CharField(max_length=40)),
                ('BDDescription', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VarName', models.CharField(max_length=40)),
                ('VarDescription', models.TextField(blank=True, null=True)),
            ],
        ),
    ]