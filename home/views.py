from django.http import FileResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def send_adstxt(request):
    temp = open('static/ads.txt', 'rb')
    response = FileResponse(temp)
    return response