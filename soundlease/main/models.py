from django.db import models
from django.utils import timezone
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField("Тег", max_length=64, help_text="Макс 64 символів", unique=True)
    slug = models.SlugField("Слаг")
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Beat(models.Model):
    title = models.CharField("Заголовок", max_length=255, help_text="Макс 255 символів")
    description = models.TextField(blank=True, verbose_name="Опис")
    pub_date = models.DateTimeField("Дата публікації", default=timezone.now)
    audio_file = models.FileField("Аудіо-файл", upload_to="beats/")
    demo_file = models.FileField("Демо-файл", upload_to="demos/", blank=True, null=True)
    cover_image = models.ImageField("Обкладинка", upload_to="covers/", default="images/default.png")
    slug = models.SlugField("Слаг", unique_for_date=pub_date)
    tag = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            pub = self.pub_date
            url = reverse("beat-detail", kwargs={"year": pub.strftime("%Y"),
                                                 "month": pub.strftime("%m"),
                                                 "day": pub.strftime("%d"),
                                                 "slug": self.slug, })
        except:
            url = "/"
        return url


    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Біт"
        verbose_name_plural = "Біти"
