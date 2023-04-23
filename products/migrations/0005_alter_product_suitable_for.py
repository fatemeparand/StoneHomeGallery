# Generated by Django 4.2 on 2023-04-21 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_stone_birth_month_stone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='suitable_for',
            field=models.CharField(choices=[('M', 'Man'), ('F', 'Woman'), ('B', 'Man and Woman')], max_length=1, verbose_name='suitable for'),
        ),
    ]
