"""
WSGI config for mywebsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

application = get_wsgi_application()

# Add WhiteNoise to serve static files in production
application = WhiteNoise(application, root=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'staticfiles'))
