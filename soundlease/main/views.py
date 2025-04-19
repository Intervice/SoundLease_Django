from django.shortcuts import render
from .models import Beat, Tag, Kit
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse


def home(request):
    return render(request, "main/main_layout.html")


class LoadMoreKits(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        kit_list = Kit.objects.all()
        paginator = Paginator(kit_list, 20)

        try:
            kits_page = paginator.page(page)
        except PageNotAnInteger:
            kits_page = paginator.page(1)
        except EmptyPage:
            kits_page = None

        if kits_page:
            kits_html_list = []
            for kit in kits_page:
                kits_html_list.append(render(request, 'main/kit_card.html',
                                             {"kit": kit}).content.decode('utf-8'))
            kits_html = "".join(kits_html_list)
            has_next = kits_page.has_next()
            next_page = kits_page.next_page_number() if has_next else None
            return JsonResponse({"kits_html": kits_html, 'has_next': has_next, "next_page": next_page})
        else:
            return JsonResponse({"kits_html": "", "has_next": False, "next_page": None})

    def get_queryset(self, **kwargs):
        return Kit.objects.all()


class KitList(ListView):
    model = Kit
    template_name = "main/kit_list.html"
    context_object_name = "kits"
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        try:
            context["Tag"] = Tag.objects.get(slug=self.kwargs.get('slug'))
        except:
            context["Tag"] = None

        kit_list = self.get_queryset()
        paginator = Paginator(kit_list, self.paginate_by)
        context['page_obj'] = paginator.page(1)

        return context

    def get_queryset(self, *args, **kwargs):
        return Kit.objects.all()


class KitDetail(DetailView):
    model = Kit
    template_name = "main/kit_detail.html"
    context_object_name = "kit"
    slug_field = "slug"
    slug_url_kwargs = "slug"

    def get_context_data(self, **kwargs):
        context = super(KitDetail, self).get_context_data(**kwargs)
        try:
            context["Tag"] = Tag.objects.get(slug=self.kwargs.get('slug'))
        except:
            context["Tag"] = None
        return context


class LoadMoreBeats(View):
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page')
        beat_list = Beat.objects.all()
        paginator = Paginator(beat_list, 20)

        try:
            beats_page = paginator.page(page)
        except PageNotAnInteger:
            beats_page = paginator.page(1)
        except EmptyPage:
            beats_page = None

        if beats_page:
            beats_html_list = []
            for beat in beats_page:
                beats_html_list.append(render(request, "main/beat_card.html",
                                              {"beat": beat}).content.decote("utf-8"))


            beats_html = "".join(beats_html_list)
            has_next = beats_page.has_next()
            next_page = beats_page.next_page_number() if has_next else None
            return JsonResponse({"beats_html": beats_html, 'has_next': has_next, "next_page": next_page})
        else:
            return JsonResponse({"beats_html": "", "has_next": False, "next_page": None})


    def get_queryset(self, **kwargs):
        return Beat.objects.all()


class BeatDetail(DetailView):
    model = Beat
    template_name = "main/beat_detail.html"
    context_object_name = "beat"
    slug_field = "slug"
    slug_url_kwargs = "slug"

    def get_context_data(self, **kwargs):
        context = super(BeatDetail, self).get_context_data(**kwargs)
        try:
            context["Tag"] = Tag.objects.get(slug=self.kwargs.get('slug'))
        except:
            context["Tag"] = None
        return context


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
