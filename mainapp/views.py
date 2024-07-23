from django.shortcuts import render

# Create your views here.
def mainview(request):
    return render(request,
                  "mainapp/main.html",
                  {})
    
def test(request):
    return render(request,
                  "mainapp/asdf.html",
                  {})