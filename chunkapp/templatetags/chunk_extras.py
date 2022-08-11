import os
from django import template
from django.conf import settings
BASE_DIR = settings.BASE_DIR

register = template.Library()

@register.filter
def filesize(value):
    """Returns the filesize of the filename given in value"""
    filepath=str(BASE_DIR)+value
    return os.path.getsize(filepath)