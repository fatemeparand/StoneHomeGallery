from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from multiselectfield import MultiSelectField
from django.urls import reverse


class Stone(models.Model):
    QUALITY_CHOICES = (
        (_('Gemstone'), _('Gemstone')),
        (_('Semiprecious stone'), _('Semiprecious stone'))
    )

    BIRTH_MONTH_STONE_CHOICES = (
        (_('farvardin'), _('farvardin')),
        (_('ordibehesht'), _('ordibehesht')),
        (_('khordad'), _('khordad')),
        (_('tir'), _('tir')),
        (_('mordad'), _('mordad')),
        (_('shahrivar'), _('shahrivar')),
        (_('mehr'), _('mehr')),
        (_('aban'), _('aban')),
        (_('azar'), _('azar')),
        (_('dey'), _('dey')),
        (_('bahman'), _('bahman')),
        (_('esfand'), _('esfand')),
    )

    stone_name = models.CharField(max_length=100, verbose_name=_('stone name'))
    stone_description = models.TextField(verbose_name=_('stone description'))
    stone_properties = models.TextField(verbose_name=_('stone properties'))
    stone_quality = models.CharField(choices=QUALITY_CHOICES, max_length=18, verbose_name=_('stone_quality'))
    birth_month_stone = MultiSelectField(choices=BIRTH_MONTH_STONE_CHOICES, max_choices=5, max_length=50,
                                         verbose_name='birth month stone')

    # birth_month_stone = models.CharField(choices=BIRTH_MONTH_STONE_CHOICES, verbose_name='birth month stone')
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
        (_('Natural Stone'), _('Natural Stone')),
        (_('Artificial Stone'), _('Artificial Stone')),
    )

    SUITABLE_CHOICES = (
        (_('Men'), _('Men')),
        (_('women'), _('Women')),
        (_('Men and Women'), _('Men and Women')),
    )

    product_name = models.CharField(max_length=200, verbose_name=_('product name'))
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, verbose_name=_('product type'))
    stone = models.ForeignKey(Stone, on_delete=models.CASCADE, related_name='stones', verbose_name=_('stone'))
    product_material = models.CharField(choices=MATERIAL_CHOICES, max_length=16, verbose_name=_('product material'))
    suitable_for = models.CharField(choices=SUITABLE_CHOICES, max_length=15, verbose_name=_('suitable for'))
    product_color = models.CharField(max_length=20, verbose_name=_('stone color'))
    product_image = models.ImageField(verbose_name=_('product image'), blank=True, upload_to='product_cover/')

    price = models.PositiveIntegerField(verbose_name=_('price'))
    product_inventory = models.PositiveIntegerField(verbose_name=_('Product inventory'))
    product_owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('product owner'))
    active = models.BooleanField(default=True, verbose_name=_('active status'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('creation date'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('Modification date'))

    def __str__(self):
        return f'product: {self.product_name}, {self.product_type}, {self.product_material}'

    class Meta:
        verbose_name_plural = _('Products')

    def get_absolute_url(self):
        return reverse('products:product_detail', args={self.id})

