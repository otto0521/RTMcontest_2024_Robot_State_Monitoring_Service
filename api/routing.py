from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/robots/", consumers.RobotStateConsumer.as_asgi()),
    path('ws/frontend/', consumers.FrontendConsumer.as_asgi()), 
]

