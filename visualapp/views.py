from django.shortcuts import render

def visual(request):
    return render(request,
                  "visualapp/visual.html",
                  {})