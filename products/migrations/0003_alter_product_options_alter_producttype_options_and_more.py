# Generated by Django 4.2 on 2023-04-21 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_active_product_product_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='producttype',
            options={'verbose_name_plural': 'Product types'},
        ),
        migrations.AlterModelOptions(
            name='stone',
            options={'verbose_name_plural': 'Stones'},
        ),
        migrations.AlterField(
            model_name='stone',
            name='birth_month_stone',
            field=models.CharField(choices=[('1', 'farvardin'), ('2', 'ordibehesht'), ('3', 'khordad'), ('4', 'tir'), ('5', 'mordad'), ('6', 'shahrivar'), ('7', 'mehr'), ('8', 'aban'), ('9', 'azar'), ('10', 'dey'), ('11', 'bahman'), ('12', 'esfand')], verbose_name='birth month stone'),
        ),
    ]
