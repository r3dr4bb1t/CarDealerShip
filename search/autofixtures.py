import random
from search.models import Car
from import_data import get_categories
from autofixture import generators, register, AutoFixture

BLUE = 'blue'
RED = 'red'
YELLOW = 'yellow'
BLACK = 'black'
WHITE = 'white'
PURPLE = 'purple'

COLOR_CHOICES = [
    (BLUE, 'blue'),
    (RED, 'red'),
    (YELLOW, 'yellow'),
    (BLACK, 'black'),
    (WHITE, 'white'),
    (PURPLE, 'purple')
]

SEOUL = 'seoul'
INCHEON = 'incheon'
DAEJEON = 'daejeon'
DAEGU = 'daegu'
BUSAN = 'busan'
GWANGJU = 'gwangju'
GYEONGGI = 'gyeonggi-do'
GANGWON = 'gangwon-do'
CHUNGBUK = 'chungbuk'
CHUNGNAM = 'chungnam'
JEONBUK = 'jeollabuk-do'
JEONNAM = 'jeollanam-do'
GYEONGBUK = 'gyeongsangbuk-do'
GYEONGNAM = 'gyeongsangnam-do'

REGION_CHOICE = [
    (INCHEON , 'incheon'),
    (DAEJEON , 'daejeon'),
    (DAEGU , 'daegu'),
    (BUSAN , 'busan'),
    (GWANGJU , 'gwangju'),
    (GYEONGGI , 'gyeonggi-do'),
    (GANGWON , 'gangwon-do'),
    (CHUNGBUK , 'chungbuk'),
    (CHUNGNAM , 'chungnam'),
    (JEONBUK , 'jeollabuk-do'),
    (JEONNAM , 'jeollanam-do'),
    (GYEONGBUK , 'gyeongsangbuk-do'),
    (GYEONGNAM , 'gyeongsangnam-do'),
]

MONTH_CHOICES = [(str(i), calendar.month_name[i]) for i in range(1, 13)]


class CarAutoFixture(AutoFixture):
    field_values={
        'model_year': generators.DateGenerator(),
        'registered_day': generators.DateGenerator(),
        'color': generators.ChoicesGenerator(COLOR_CHOICES),
        'fuel': generators.ChoicesGenerator(Car.FUEL_CHOICES),
        'gear': generators.ChoicesGenerator(Car.GEAR_CHOICES),
        'kms': generators.PositiveIntegerGenerator(),
        'region': generators.ChoicesGenerator(REGION_CHOICE),
        'status': generators.ChoicesGenerator(Car.STATUS_CHOICES),
    }

register(Car, CarAutoFixture )
#
# model_year = YearMonthField(max_length=20)
# registered_day = models.DateTimeField('Registered Date')
# brand = models.CharField(max_length=100)
# type = models.CharField(max_length=100)
# model = models.CharField(max_length=100)
# color = models.CharField(max_length=20)
# fuel = models.CharField(
#     max_length=6,
#     choices=FUEL_CHOICES,
#     default=GASOLINE,
# )
# gear = models.CharField(
#     max_length=4,
#     choices=GEAR_CHOICES,
#     default=AUTO,
# )
# kms = models.IntegerField(null=True)
# region = models.CharField(max_length=30)
# status = models.CharField(
#     max_length=7,
#     choices=STATUS_CHOICES,
#     default=PENDING,
# )
# photo = models.Im
#  연료(lpg, gasoline(휘발유), diesel(디젤), hybrid(하이브리드), electric(전기)
#     bifuel(바이퓨얼)
#     변속기(auto(자동), manual(수동)
