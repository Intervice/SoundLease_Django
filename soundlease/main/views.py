from django.shortcuts import render
from .models import Beat, Tag
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def home(request):
    return render(request, "main/index.html")


class LoadMoreBeats(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        beat_list = Beat.objects.all()
        paginator = Paginator(beat_list, 20)

        try:
            beats = paginator.page(page)
        except PageNotAnInteger:
            beats = paginator.page(1)
        except EmptyPage:
            beats = None

        if beats:
            beats_html = render(request, 'main/beat_card.html', {"beat": beat for beat in beats})
            has_next = beats.has_next()
            next_page = beats.next_page_number() if has_next else None
            return JsonResponse({"beats_html": beats_html, 'has_next': has_next, "next_page": next_page})
        else:
            return JsonResponse({"beats_html": "", "has_next": False, "next_page": None})


    def get_queryset(self, **kwargs):
        return Beat.objects.all()


class BeatList(ListView):
    model = Beat
    template_name = "main/beat_list.html"
    context_object_name = "beats"
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            context["Tag"] = Tag.objects.get(slug=self.kwargs.get('slug'))
        except:
            context["Tag"] = None

        beat_list = self.get_queryset()
        paginator = Paginator(beat_list, self.paginate_by)
        context['page_obj'] = paginator.page(1)

        return context

    def get_queryset(self, *args, **kwargs):
        return Beat.objects.all()
        # queryset = Beat.objects.all()
        # tag_slug = self.kwargs.get('slug')
        # if tag_slug:
        #     try:
        #         tag = Tag.objects.get(slug=tag_slug)
        #         queryset = queryset.filter(tags=tag)
        #     except:
        #         queryset = Beat.objects.none()
        # return queryset

