from django import forms
from .models import Beat, Tag, Kit

class BeatForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False, label="Теги")
    cover_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={"multiple": False}))
    audio_file = forms.FileField(required=True, label="Аудіо файл")
    demo_file = forms.FileField(required=False, label="Демо версія")
    description = forms.CharField(widget=forms.Textarea, required=False, label='Опис')
    pub_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))


    class Meta:
        model = Beat
        fields = "__all__"


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
