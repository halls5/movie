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
    
<<<<<<< HEAD


def quest(request):
    return render(request,
                  "movieapp/quest.html",
                  {})
    
def test1(request):
    return render(request,
                  "movieapp/quest17.html",
                  {})
    
=======
def templateLayout(request):
    return render(request,
                  "movieapp/extend/template_layout.html",
                  {})
def signup(request):
    return render(request,
                  "movieapp/signup.html",
                  {})
>>>>>>> 64437b19bcb94f6e96d46e2fa554c663b7942d49
