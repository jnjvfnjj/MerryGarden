from django.shortcuts import render
from homework.models import Settings, Gallery, About, Contact, News,Post, Team

# Create your views here.
def index(request):
    settings = Settings.objects.latest("id")
    return render(request, "index.html", locals())

def gallery(request):
    photo = Gallery.objects.latest("id")
    return render(request, "gallery.html", locals())

def about(request):
    about = About.objects.latest("id")
    return render(request, "about.html", locals())

def contact(request):
    contact = Contact.objects.latest("id")
    return render(request, "contact.html", locals())

def news(request):
    news = News.objects.latest("id")
    return render(request, "news.html", locals())

def post(request):
    post = Post.objects.latest("id")
    return render(request, "post.html",locals())

def team(request):
    team = Team.objects.latest("id")
    return render(request, "team.html", locals())


