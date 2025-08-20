from django.shortcuts import HttpResponse, render

def home_index(request):
    return render(request, 'index_home.html')