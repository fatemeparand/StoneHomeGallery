# Generated by Django 4.2 on 2023-04-23 13:59

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_stone_stone_quality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stone',
            name='birth_month_stone',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('farvardin', 'farvardin'), ('ordibehesht', 'ordibehesht'), ('khordad', 'khordad'), ('tir', 'tir'), ('mordad', 'mordad'), ('shahrivar', 'shahrivar'), ('mehr', 'mehr'), ('aban', 'aban'), ('azar', 'azar'), ('dey', 'dey'), ('bahman', 'bahman'), ('esfand', 'esfand')], max_length=50, verbose_name='birth month stone'),
        ),
        migrations.AlterField(
            model_name='stone',
            name='stone_quality',
            field=models.CharField(choices=[('Gemstone', 'Gemstone'), ('Semiprecious stone', 'Semiprecious stone')], max_length=18, verbose_name='stone_quality'),
        ),
    ]