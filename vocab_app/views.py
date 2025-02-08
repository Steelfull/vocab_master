from django.shortcuts import render

def home(request):
    return render(request, 'vocab_app/home.html')