from django.urls import path
from .views import home, KitList, LoadMoreKits, BeatList, LoadMoreBeats, KitDetail, BeatDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", home, name="home"),
    path(r"kits/", KitList.as_view(), name="kit-list"),
    path(r"load-more-kits/", LoadMoreKits.as_view(), name="load-more-kits"),
    path(r"kits/<slug:slug>", KitDetail.as_view(), name="kit-detail"),
    path(r"beats/", BeatList.as_view(), name="beat-list"),
    path("load-more-beats/", LoadMoreBeats.as_view(), name="load-more-beats"),
    path(r"beats/<slug:slug>", BeatDetail.as_view(), name="beat-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
