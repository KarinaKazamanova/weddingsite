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
    'После церемонии планируется небольшой фуршет, который пройдет по адресу. г. Москва, Русаковская улица, 24. Отель - Holyday Inn',
    f'Просим {persons_count} не дарить нам цветы - сразу после свадьбы мы улетаем в свадебное путешествие и не успеем насладиться их красотой.',
    'Мы будем рады видеть Вас на нашем торжестве.',
    ]

def index(request):
    logger.info('Index page accessed')
    return TemplateResponse(request, 'layout.html').render()

def mom(request):
    ending = 'ая'
    name = 'мамочка'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()    
    
def father(request):
    ending = 'ой'
    name = 'папа'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def alexandr_and_irina(request):
    ending = 'ие'
    name = 'дядя Саша и тётя Ира'
    persons_count = 'вас'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def maria(request):
    ending = 'ая'
    name = 'Маша'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def anna(request):
    ending = 'ая'
    name = 'Аня'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def julia_and_artem(request):
    ending = 'ие'
    name = 'Юлия и Артём'
    persons_count = 'ваc'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
def nastya_and_alan(request):
    ending = 'ие'
    name = 'Настя и Алан'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def gasan(request):
    ending = 'ие'
    name = 'Гасан и твоя спутница'
    persons_count = 'ваc'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
    
def nikita(request):
    ending = 'ие'
    name = 'Никита и твоя спутница'
    persons_count = 'ваc'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()  
    
def egor(request):
    ending = 'ой'
    name = 'Егор'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render() 
    
def aina_and_latifa(request):
    ending = 'ие'
    name = 'Айна и Латифа'
    persons_count = 'вас'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def sveta(request):
    ending = 'ая'
    name = 'Света'
    persons_count = 'тебя'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'relatives_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    
def tatiana(request):
    ending = 'ая'
    name = 'тетя Таня'
    persons_count = 'Вас'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render()
    

    
def nikita_and_olya(request):
    ending = 'ие'
    name = 'Никита и Оля'
    persons_count = 'ваc'
    logger.info('Index page accessed')
    return TemplateResponse(request, 'friends_layout.html',
                            {'ending': ending,
                             'name': name,
                             'persons_count': persons_count,
                                }).render() 
    
    

    

    
    

    
 