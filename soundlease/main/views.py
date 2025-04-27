from django.shortcuts import render, redirect
from .models import Beat, Tag, Kit
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from itertools import chain
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def publishing(request):
    if request.user.is_authenticated:
        return

    return render(request, "main/publish_not_register.html")

def logout_func(request):
    logout(request)
    return redirect("home")

def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(f" {username} {password}")

        if not username or not password:
            messages.error(request, "Не всі поля заповнені.")
            return render(request, "main/login_page.html")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Немає акаунту з таким іменем.")
            return render(request, "main/login_page.html")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Неправильний пароль.")
            return render(request, "main/login_page.html")
    return render(request, "main/login_page.html")


def register(request):
    if request.method == "POST":
        # print("REQUEST POST DATA:")
        # print(request.POST)

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm-password_value")

        # print(f"Username: '{username}'")
        # print(f"Email: '{email}'")
        # print(f"Password: '{password}'")
        # print(f"Confirm Password: '{confirm_password}'")

        if not username or not email or not password or not confirm_password:
            messages.error(request, "Не всі поля заповнені.")
            return render(request, "main/reg_page.html")

        print(f"Confirm Password BEFORE CHECK: '{confirm_password}'")

        if password != confirm_password:
            messages.error(request, "Паролі не збігаються.")
            return render(request, "main/reg_page.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Дане ім'я вже зайнято.")
            return render(request, "main/reg_page.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Дана пошта вже зайнята.")
            return render(request, "main/reg_page.html")


        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, "Реєстрація успішна.")
        return redirect("home")

    return render(request, "main/reg_page.html")


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        kits = Kit.objects.all()[:4]
        beats = Beat.objects.all()[:5]

        combined = list(chain(
            [{'type': 'kit', 'data': kit} for kit in kits],
            [{'type': 'beat', 'data': beat} for beat in beats]
        ))
        context = {'combined_objects': combined}
        return render(request, 'main/main_page.html', context)


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
                                              {"beat": beat}).content.decode("utf-8"))


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
