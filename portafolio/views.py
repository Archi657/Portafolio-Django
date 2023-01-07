from django.shortcuts import render
from .models import Projects
from bs4 import  BeautifulSoup as bs
import requests, re

def home(request):
    projects = Projects.objects.all()
    url = "https://juliang.hashnode.dev"
    page = requests.get(url)
    soup = bs(page.content, "html.parser")
    posts = soup.find_all('div', {'class':'blog-post-card css-16gx0ij'})
    posts_ = []
    for post in posts:
        posts_.append(str(post))
    these_regex="<a[^>]*>([^<]+)</a>"
    pattern=re.compile(these_regex)
    posts_clean=[]
    for post in posts_:
        posts_clean.append(re.findall(pattern,post))

    return render(request, 'home.html', {'projects' : projects ,'posts' : posts_clean})
