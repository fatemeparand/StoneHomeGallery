# Generated by Django 4.2 on 2023-04-21 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(verbose_name='product type')),
            ],
        ),
        migrations.CreateModel(
            name='Stone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stone_name', models.CharField(max_length=100, verbose_name='stone name')),
                ('stone_description', models.TextField(verbose_name='stone description')),
                ('stone_properties', models.TextField(verbose_name='stone properties')),
                ('stone_quality', models.CharField(choices=[('gen', 'Gemstone'), ('semi', 'Semiprecious stone')], verbose_name='stone_quality')),
                ('birth_month_stone', models.TextField(verbose_name='birth month stone')),
                ('stone_image', models.ImageField(upload_to='stone_cover/', verbose_name='stone image')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200, verbose_name='product name')),
                ('product_material', models.CharField(choices=[('natural', 'Natural Stone'), ('artificial', 'Artificial Stone')], max_length=10, verbose_name='product material')),
                ('suitable_for', models.CharField(choices=[('M', 'Man'), ('F', 'Woman')], max_length=1, verbose_name='suitable for')),
                ('product_color', models.CharField(max_length=20, verbose_name='stone color')),
                ('product_image', models.ImageField(upload_to='product_cover/', verbose_name='product image')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('Product_inventory', models.PositiveIntegerField(verbose_name='Product_inventory')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producttype', verbose_name='product type')),
                ('stone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stones', to='products.stone', verbose_name='stone')),
            ],
        ),
    ]
