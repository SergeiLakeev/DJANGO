from django.shortcuts import render
from .models import Advertisement

def index(reqest):
    advertisement = Advertisement.objects.all()
    context = {'advertisement':advertisement}
    return render(reqest, 'index.html', context)


def top_sellers(reqest):
    return render(reqest, 'top-sellers.html')