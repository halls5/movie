from django.shortcuts import render

# Create your views here.

def quest(request):
    return render(request,
                  "recoapp/quest.html",
                  {})