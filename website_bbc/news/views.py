from django.shortcuts import render

from news.models import News
from events.models import File

def index(request):
    news_list = News.objects.order_by('-date')
    context_dict = {'news_list' : news_list }
    return render(request, 'news/index.html', context_dict)

def news_details(request, news_slug):
    context_dict = {}
    try:
        news = News.objects.get(slug=news_slug)
        context_dict['news'] = news
        files = File.objects.filter(set=news.uploaded_files)
        context_dict['files'] = files
    except News.DoesNotExist:
        pass

    return render(request, 'news/details.html', context_dict)
