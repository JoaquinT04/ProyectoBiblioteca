from __future__ import absolute_import  # Solo si usas python 2



from django.contrib.staticfiles.storage import staticfiles_storage

from django.core.urlresolvers import reverse



from jinja2 import Environment





def ini_jinja2(**options):

    env = Environment(**options)

    env.globals.update({

        'static': staticfiles_storage.url,

        'url': reverse,

    })

    return env