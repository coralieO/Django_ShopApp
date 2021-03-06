"""
ASGI config for Django project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import tchat.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

application = ProtocolTypeRouter({
  'http': get_asgi_application(),
  # 'websocket': URLRouter(
  #     tchat.routing.websocket_urlpatterns
  #   ),
  'websocket': AuthMiddlewareStack(  
        URLRouter(
            tchat.routing.websocket_urlpatterns
        )
    ),  
})
