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
    


def quest(request):
    return render(request,
                  "movieapp/quest.html",
                  {})
    
def test1(request):
    return render(request,
                  "movieapp/quest17.html",
                  {})
    
