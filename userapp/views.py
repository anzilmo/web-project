from django.shortcuts import render

# Create your views here.
def index(requste):
    return render(requste,'index.html')
