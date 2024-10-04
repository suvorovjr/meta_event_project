from django.urls import path
from .apps import EventsConfig
from .views import GetFacebookPagesAPIView

app_name = EventsConfig.name

urlpatterns = [
    path('get_fb_pages/', GetFacebookPagesAPIView.as_view(), name='get_fb_pages')
]
