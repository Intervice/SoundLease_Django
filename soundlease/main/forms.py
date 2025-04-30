from django import forms
from .models import Beat, Tag, Kit
from django.core.validators import MinValueValidator


class BeatForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False, label="Теги")
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple": False}), required=False)
    audio_file = forms.FileField(required=True, label="Аудіо файл")
    demo_file = forms.FileField(required=False, label="Демо версія")
    description = forms.CharField(widget=forms.Textarea, required=False, label='Опис')
    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Ціна",
                                validators=[MinValueValidator(0.00)], initial=0.00)
    premium_price = forms.DecimalField(max_digits=10, decimal_places=2, label="Преміум ціна",
                                        validators=[MinValueValidator(0.00)], required=False, initial=0.00)

    class Meta:
        model = Beat
        fields = ['title', 'audio_file', 'demo_file', 'cover_image', 'description', 'pub_date', 'tags', 'price',
                  'premium_price']


class KitForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False, label="Теги")
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple": False}))
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={"multiple": False}))

    description = forms.CharField(widget=forms.Textarea, required=False, label='Опис')
    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    license_info = forms.CharField(widget=forms.Textarea, required=False, label="Ліцензія")


    class Meta:
        model = Kit
        fields = "__all__"
