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




def index(request):
    # with open ('myapp\\templates\index_alternative.html', 'r', encoding='utf-8') as file:
    #     html = file.read()
    # return HttpResponse(html)
    # return render(request, 'index.html')
    return TemplateResponse(request, 'index.html').render()
    