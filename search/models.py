import datetime
import mptt
import time
from django.db import models
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django import template
register = template.Library()


from mptt.models import TreeForeignKey, MPTTModel
from django.contrib.auth.models import Group

# Create your models here.
YEARMONTH_INPUT_FORMATS = (
    '%Y-%m', '%m/%Y', '%m/%y', # '2006-10', '10/2006', '10/06'
)


class YearMonthField(models.CharField):
    default_error_messages = {
        'invalid': _('Enter a valid year and month.'),
    }

    def __init__(self, input_formats=None, *args, **kwargs):
        super(YearMonthField, self).__init__(*args, **kwargs)
        self.input_formats = input_formats

    def clean(self, value):
        if value in self.validators.EMPTY_VALUES:
            return None
        if isinstance(value, datetime.datetime):
            return format(value, '%Y-%m')
        if isinstance(value, datetime.date):
            return format(value, '%Y-%m')
        for fmt in self.input_formats or YEARMONTH_INPUT_FORMATS:
            try:
                date = datetime.date(*time.strptime(value, fmt)[:3])
                return format(date, '%Y-%m')
            except ValueError:
                continue
        raise ValidationError(self.error_messages['invalid'])


class Make(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Model(models.Model):
    name = models.CharField(max_length=40)
    make =  models.ForeignKey(Make, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class SubModel(models.Model):
    name = models.CharField(max_length=50)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    model_year = YearMonthField(max_length=20)

    def __str__(self):
        return str(self.name)


# TreeForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True).contribute_to_class(Group, 'Make')
# mptt.register(Group, order_insertion_by=['name'])


class Car(models.Model):
    LPG = 'LPG'
    GASOLINE = 'GAS'
    DIESEL = 'DIESEL'
    HYBRID = 'HYBRID'
    ELECTRIC = 'ELEC'
    BIFUEL = 'BI'
    FUEL_CHOICES = [
        (LPG, 'lpg'),
        (GASOLINE, 'gasoline'),
        (DIESEL, 'diesel'),
        (HYBRID, 'HYBRID'),
        (ELECTRIC, 'electric'),
        (BIFUEL, 'bi_fuel'),
    ]

    AUTO = 'AUTO'
    MANUAL = 'MAN'
    GEAR_CHOICES = [
        (AUTO, 'auto'),
        (MANUAL, 'manual'),
    ]

    PENDING = 'pend'
    INAUCTION = 'auction'



    DONEAUCTION = 'done'

    STATUS_CHOICES = [
        (PENDING, 'pending'),
        (INAUCTION, 'in_auction'),
        (DONEAUCTION, 'done_auction')

    ]
    registered_day = models.DateField('Registered Date')
    sub_model = models.ForeignKey(SubModel, on_delete=models.CASCADE, null=True)
    color = models.CharField(max_length=20)
    fuel = models.CharField(
        max_length=6,
        choices=FUEL_CHOICES,
        default=GASOLINE,
    )
    gear = models.CharField(
        max_length=4,
        choices=GEAR_CHOICES,
        default=AUTO,
    )
    kms = models.IntegerField(null=True)
    region = models.CharField(max_length=30)
    status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    photo = models.ImageField(null=True)

    def __str__(self):
        return str(self.sub_model)
