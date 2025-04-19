from django.contrib import admin
from .models import Tag, Beat, Kit


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
    raw_id_fields = ("tags",)
    fieldsets = (
        ("", {
            "fields": ("pub_date", "title", "author", "price", "premium_price", "description", "cover_image", "audio_file",
                       "demo_file", "tags")
        }),
        (("Додатково",), {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("slug",),
         }),
    )

class KitAdmin(admin.ModelAdmin):
    list_display = ("title", "pub_date", "cover_image")
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("tags",)
    fieldsets = (
        ("", {
            "fields": ("pub_date", "title", "author", "price", "premium_price", "description", "cover_image", "file",
                       "license_info", "tags")
        }),
        (("Додатково",), {
            "classes": ("grp-collapse grp-closed",),
            "fields": ("slug",),
        }),
    )


admin.site.register(Tag, TagAdmin)
admin.site.register(Beat, BeatAdmin)
admin.site.register(Kit, KitAdmin)
