from django.shortcuts import render

# Create your views here.

def quest(request):
    return render(request,
                  "recoapp/quest.html",
                  {})
    
def keyword(request):
    return render(request,
                  "recoapp/keyword.html",
                  {})
    
def random(request):
    return render(request,
                  "recoapp/random.html",
                  {})
    
def random_result(request):
    return render(request,
                  "recoapp/random_result.html",
                  {})
    
def keyword_result(request):
    return render(request,
                  "recoapp/keyword_result.html",
                  {})