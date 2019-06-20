import datetime
import time
from django.db import models
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

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
    model_year = YearMonthField(max_length=20)
    registered_day = models.DateTimeField('Registered Date')
    brand = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
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
