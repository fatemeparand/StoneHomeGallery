from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class Stone(models.Model):
    QUALITY_CHOICES = (
        ('gen', 'Gemstone'),
        ('semi', 'Semiprecious stone')
    )

    BIRTH_MONTH_STONE_CHOICES = (
        ('1', _('farvardin')),
        ('2', _('ordibehesht')),
        ('3', _('khordad')),
        ('4', _('tir')),
        ('5', _('mordad')),
        ('6', _('shahrivar')),
        ('7', _('mehr')),
        ('8', _('aban')),
        ('9', _('azar')),
        ('10', _('dey')),
        ('11', _('bahman')),
        ('12', _('esfand')),
    )

    stone_name = models.CharField(max_length=100, verbose_name=_('stone name'))
    stone_description = models.TextField(verbose_name=_('stone description'))
    stone_properties = models.TextField(verbose_name=_('stone properties'))
    stone_quality = models.CharField(choices=QUALITY_CHOICES, verbose_name=_('stone_quality'))
    birth_month_stone = models.CharField(choices=BIRTH_MONTH_STONE_CHOICES, verbose_name='birth month stone')
    stone_image = models.ImageField(verbose_name=_('stone image'), upload_to='stone_cover/')

    def __str__(self):
        return self.stone_name

    class Meta:
        verbose_name_plural = _('Stones')


class ProductType(models.Model):
    type = models.CharField(verbose_name=_('product type'))

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = _('Product types')


class Product(models.Model):

    MATERIAL_CHOICES = (
        ('natural', 'Natural Stone'),
        ('artificial', 'Artificial Stone'),
    )

    SUITABLE_CHOICES = (
        ('M', 'Man'),
        ('F', 'Woman')
    )

    product_name = models.CharField(max_length=200, verbose_name=_('product name'))
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name=_('product type'))
    stone = models.ForeignKey(Stone, on_delete=models.CASCADE, related_name='stones', verbose_name=_('stone'))
    product_material = models.CharField(choices=MATERIAL_CHOICES, max_length=10, verbose_name=_('product material'))
    suitable_for = models.CharField(choices=SUITABLE_CHOICES, max_length=1, verbose_name=_('suitable for'))
    product_color = models.CharField(max_length=20, verbose_name=_('stone color'))
    product_image = models.ImageField(verbose_name=_('product image'), upload_to='product_cover/')

    price = models.PositiveIntegerField(verbose_name=_('price'))
    Product_inventory = models.PositiveIntegerField(verbose_name=_('Product_inventory'))
    product_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('product owner'))
    active = models.BooleanField(default=True, verbose_name=_('active status'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Modification date'))

    def __str__(self):
        return f'product: {self.product_name}, {self.product_type}, {self.product_material}'

    class Meta:
        verbose_name_plural = _('Products')
