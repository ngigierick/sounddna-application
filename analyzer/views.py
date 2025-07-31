from django.http import HttpResponse

def home(request):
    return HttpResponse("🎧 Hello from the Sound Analyzer App!")


from django.shortcuts import render

def home(request):
    return render(request, 'analyzer/home.html')
