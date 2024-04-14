import datetime
import logging
import pathlib

from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
# from .models import Order, User,OrderProduct, Product
from django.utils import timezone
# from .forms import *
from django.core.files.storage import FileSystemStorage

logger = logging.getLogger(__name__)



FRIENDS_MESSAGE = f"""на фуршет по случаю нашего бракосочетания, который состоится 29 июня 2024 года в 13 часов 15 минут по адресу:___.
После церемонии планируется небольшой фуршет, который пройдет по адресу. 
Просим Вас не дарить нам цветы - сразу после свадьбы мы улетаем в свадебное путешествие и не успеем насладиться их красотой.
Мы будем рады видеть Вас на нашем торжестве. 
P.S.:пожалуйста, подтвердите Ваше присутствие на нашем празднике до 20 июня 2024 года любым удобным для вас способом."""


def _relative_message(persons_count: str):
    return [
    f'Приглашаем {persons_count} на торжественную церемонию по случаю нашего бракосочетания, которая состоится 29.06.2024 г. в 13:15 по адресу: г. Москва, Малый Харитоньевский пер., д. 10, стр. 1.!',
    'После церемонии планируется небольшой фуршет, который пройдет по адресу.',
    'Просим Вас не дарить нам цветы - сразу после свадьбы мы улетаем в свадебное путешествие и не успеем насладиться их красотой.',
    'Мы будем рады видеть Вас на нашем торжестве.',
    ]

def index(request):
    logger.info('Index page accessed')
    return TemplateResponse(request, 'layout.html').render()

def mom(request):
    ending = 'ая'
    name = 'мамочка'
    persons_count = 'тебя'
    message = _relative_message(persons_count=persons_count)
    logger.info('Index page accessed')
    return TemplateResponse(request, 'layout.html',
                            {'ending': ending,
                             'name': name,
                             'message': message,
                                }).render()    
    
def father(request):
    ending = 'ой'
    name = 'отец'
    persons_count = 'тебя'
    event = 'Церемония состоится 29.06.2024 в 13:15 по адресу'
    adress = 'г. Москва, Малый Харитоньевский пер., д. 10, стр. 1'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                             'event': event,
                             'adress': adress,
                                }).render() 