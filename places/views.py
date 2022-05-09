from django.shortcuts import render

# Create your views here.

def place(request):
    return render(request,'places.html')
