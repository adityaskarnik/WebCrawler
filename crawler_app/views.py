from django.http import HttpResponse
from django.shortcuts import render, redirect
from crawler_app import url_links
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib import messages

def index(request):
    return render(request, 'main.html')

def submit(request):
    images = []
    post_data = request.GET.dict()
    url = post_data.get("url")
    depth = post_data.get("depth")
    try:
        val = int(depth)
        try:
            validate = URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
            validate(url)
            images = url_links.get_images(url, depth)
            return render(request, 'home.html', {'images':images, 'url':url, 'depth':depth})
        except Exception:
            messages.error(request,'Enter a valid URL')
            return render(request, 'main.html', {})
    except ValueError:
        messages.error(request,'Enter a valid number for depth')
        return render(request , 'main.html' , {})    