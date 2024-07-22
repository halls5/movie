from django.shortcuts import render

# Create your views here.

def mainview(request):
    return render(request,
                  "movieapp/main.html",
                  {})
    
def login(request):
    return render(request,
                  "movieapp/login.html",
                  {})
    
    
def main2(request):
    return render(request,
                  "movieapp/main2.html",
                  {})
    
def templateLayout(request):
    return render(request,
                  "movieapp/extend/template_layout.html",
                  {})
    