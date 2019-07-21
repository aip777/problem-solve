from django.shortcuts import render

# Create your views here.





def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})


def demo_view(request, *args, **kwargs):
    return render(request, 'demo.html', {})