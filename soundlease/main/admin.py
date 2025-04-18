from django.contrib import admin
from django.shortcuts import get_object_or_404
from .models import Tag, Beat
from .forms import BeatForm


class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        ("", {
            "fields": ("name", "slug",),
        },),
    )


class BeatAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "cover_image")
    prepopulated_fields = {"slug": ("title",)}
    # multiupload_form = False
    # multiupload_list = False
    raw_id_fields = ("tags",) #
    fieldsets = (
        ("", {
            "fields": ("pub_date", "title", "author", "price", "description", "cover_image", "audio_file", "demo_file", "tags")
        }),
        (("Додатково",), {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("slug",),
         }),
    )


admin.site.register(Tag, TagAdmin)
admin.site.register(Beat, BeatAdmin)
