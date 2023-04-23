# Generated by Django 4.2 on 2023-04-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_stone_birth_month_stone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stone',
            name='stone_quality',
            field=models.CharField(choices=[('Gemstone', 'Gemstone'), ('Semiprecious stone', 'Semiprecious stone')], max_length=50, verbose_name='stone_quality'),
        ),
    ]
