# import django
# django.setup()
# from django.conf import settings
# settings.configure()
# import sys
# sys.path.append("..")
from .models import equipMall

test1 = equipList(
    identification='123456789',
    name='测试样例',
    price='300',
    link='http://www.baidu.com'
)
test1.save()
