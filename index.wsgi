import os
import sys
 
sys.path.append('/home/c/cc07149/tdzpu/public_html/tdzpu/')
sys.path.append('home/c/cc07149/tdzpu/public_html/myenv/lib/python3.6/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tdzpu.settings'
import django
django.setup()
 
from django.core.handlers import wsgi
application = wsgi.WSGIHandler()
