from django.shortcuts import render
from .models import Beat, Tag
from django.views.generic import ListView

def home(request):
    return render(request, "main/index.html")

class BeatList(ListView):
    model = Beat
    template_name = "main/beat_list.html"
    context_object_name = "beats"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            context["Tag"] = Tag.objects.get(slug=self.kwargs.get('slug'))
        except:
            context["Tag"] = None

        return context

    def get_queryset(self, *args, **kwargs):
        return Beat.objects.all()
