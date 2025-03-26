import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for the 'application' variable.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practise1.settings')

application = get_wsgi_application()
