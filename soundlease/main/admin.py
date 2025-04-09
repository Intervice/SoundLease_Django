from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Tag, Beat
from .forms import BeatForm


class TagAdmin(admin.ModelAdmin):
    pass


class BeatAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)

admin.site.register(Beat, BeatAdmin)
