import os

from dj_static import Cling
from django.core.wsgi import get_wsgi_application
from whitenoise.Django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sample_project.settings")

application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)
# application = get_wsgi_application()