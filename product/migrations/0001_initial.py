# Generated by Django 5.1.7 on 2025-03-23 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Ad')),
                ('surname', models.CharField(max_length=300, verbose_name='Soyad')),
                ('age', models.PositiveIntegerField(verbose_name='Yaş')),
                ('birthday', models.DateField(verbose_name='Doğum tarixi')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Ad')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Ad')),
                ('price', models.FloatField(verbose_name='Qiymət')),
                ('tax_price', models.FloatField(blank=True, null=True, verbose_name='Tax qiymət')),
                ('discount_price', models.FloatField(blank=True, null=True, verbose_name='Endirimli qiymət')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Yaranma tarixi')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tarixi')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.author')),
                ('tags', models.ManyToManyField(blank=True, to='product.tag', verbose_name='Tag')),
            ],
        ),
    ]
