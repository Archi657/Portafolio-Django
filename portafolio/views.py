from django.shortcuts import render
from .models import Projects
from bs4 import  BeautifulSoup as bs
import requests, re

def getPhotoPost(url):
    pattern = re.compile("""(<img alt="[\w :.-]+)" src="([a-z:/;\d,A-Z"\s=-]+)%([a-z:/;\d,A-Z"\s=-]+)%([a-z:/;\d,A-Z"\s=-]+)%([a-z:/;\d,A-Z"\s=-]+)%([a-z:/;\d,A-Z"\s=-]+)%([a-z:/;\d,A-Z"\s=-]+)%([a-zA-Z\d\s!$%^&*()@#_+|~=`{}\[\]:;"'?,.\/]+)-(\n?image:url[(&quot;]+)(https:\/\/cdn.hashnode.com\/res\/hashnode\/image\/upload\/[A-Za-z\d\/.]+)""")
    page = requests.get(url)
    matches = pattern.finditer(page.text)
    PhotosURL = []
    for match in matches:
        PhotosURL.append(match.group(10))
    return PhotosURL

def getDescriptioAndURL(url):
    pattern = re.compile(r"""(<p class="blog-post-card-brief css-etf49e">)+(\t*\s*)?(<a aria-label="[:a-zA-Z\s\d-]+("\shref="))([a-zA-Z\]é+")([\d\sa-zA-Z-!$%^&*()@#_+|~=`{}\[\]:";'?,.\/]+)>(\t*\s*)?([a-zA-Z\]é+)">([\d\sa-zA-Z-!$%^&*()@#_+|~=`{}\[\]:";'?,.\/]+)""")
    page = requests.get(url)
    matches = pattern.finditer(page.text)
    descriptionurl = []
    for match in matches:
        descriptionurl.append({ 'link' : match.group(5), 'desc' : match.group(7) })
    return descriptionurl

def getTitle(url):
    pattern = re.compile(r'(<h1 class="blog-post-card-title css-c643t4">+)(\t*\s*)+(<a\t*\s*aria-label=")+([\w\s\d:-]+)+([\w\s\d:-]+)"\shref="(https:\/\/juliang\.hashnode\.dev\/[\w-]+)')
    page = requests.get(url)
    matches = pattern.finditer(page.text)
    titles = []
    for match in matches:
        titles.append(match.group(4))
    return titles

def home(request):
    projects = Projects.objects.all()
    url = "https://juliang.hashnode.dev"

    # Photos Url
    photos = getPhotoPost(url)

    # Description and Url
    desc_url = getDescriptioAndURL(url)

    # Titles
    titles = getTitle(url)

    posts=[]

    for i, photo in enumerate(photos):
        post = {
            'title' : titles[i],
            'img' : photo,
            'desc' : desc_url[i]['desc'],
            'url' : desc_url[i]['link']
        }
        posts.append(post)

    return render(request, 'home.html', {'projects' : projects ,'posts' : posts })
