from django.urls import path
from .views import home, BeatList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path(r"beats", BeatList.as_view(), name="beat-list")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
