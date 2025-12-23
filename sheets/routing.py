from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/sheets/(?P<sheet_id>\w+)/$', consumers.SheetConsumer.as_asgi()),
]
