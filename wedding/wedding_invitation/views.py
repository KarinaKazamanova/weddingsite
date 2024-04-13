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


def index(request):
    logger.info('Index page accessed')
    return TemplateResponse(request, 'layout.html').render()
    