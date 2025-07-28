from django.shortcuts import render

# Create your views here.


def helo(request):
    return render(request,'layout.html')