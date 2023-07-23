from django.shortcuts import render
from django.http import HttpResponse

def index(reqest):
    return render(reqest, 'index.html')
def top_sellers(reqest):
    return render(reqest, 'top-sellers.html')