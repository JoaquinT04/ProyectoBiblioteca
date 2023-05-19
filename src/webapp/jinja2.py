from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
#from webapp.jinja2 import Environment
#import webapp.jinja2 as jinja2
import jinja2


def ini_jinja2(**options):
    env = jinja2.Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
    })
    return env

