from django.core.validators import MinValueValidator
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
    author = models.CharField("Автор", max_length=64, help_text="Макс 64 символа", default="Unknown")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна",
                                validators=[MinValueValidator(0.00)], default=0.00)
    premium_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Преміум ціна",
                                        validators=[MinValueValidator(0.00)], default=0.00)
    description = models.TextField(blank=True, verbose_name="Опис")
    pub_date = models.DateTimeField("Дата публікації", default=timezone.now)
    audio_file = models.FileField("Аудіо-файл", upload_to="beats/")
    demo_file = models.FileField("Демо-файл", upload_to="demos/", blank=True, null=True)
    cover_image = models.ImageField("Обкладинка", upload_to="covers/", default="img/default.png")
    slug = models.SlugField("Слаг")
    tags = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            url = reverse("beat-detail", kwargs={"slug": self.slug, })
        except:
            url = "/"
        return url


    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Біт"
        verbose_name_plural = "Біти"


class Kit(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва набору", help_text="Макс 255 символів")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Слаг")
    description = models.TextField(blank=True, verbose_name="Опис")
    cover_image = models.ImageField(upload_to='kits/covers/', default="img/default.png", verbose_name="Обкладинка")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна",
                                validators=[MinValueValidator(0.00)], default=0.00)
    premium_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Преміум ціна",
                                validators=[MinValueValidator(0.00)], default=0.00)
    author = models.CharField("Автор", max_length=64, help_text="Макс 64 символа", default="Unknown")
    pub_date = models.DateTimeField("Дата публікації", default=timezone.now)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", blank=True)
    license_info = models.TextField(blank=True, verbose_name="Інформація про ліцензію")
    file = models.FileField(upload_to='kits/files/', verbose_name="Файли набору (ZIP)", blank=False, null=False,
                            default='kits/files/icon.7z')

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = "Кіт"
        verbose_name_plural = "Кіти"

    def get_absolute_url(self):
        try:
            url = reverse('kit-detail', kwargs={'slug': self.slug})
        except:
            url = "/"
        return url
