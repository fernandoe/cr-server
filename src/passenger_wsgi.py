import os
import sys

import django.core.handlers.wsgi

INTERP = "/home/dh_gr97s7/venv-app-3.11.6/bin/python3"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, "/home/dh_gr97s7/cr.controlederisco.com.br")

os.environ["DJANGO_SETTINGS_MODULE"] = "server.settings.dreamhost"
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
