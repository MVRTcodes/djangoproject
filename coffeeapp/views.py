from django.http.response import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return render(request, 'about.html')

def projects(request):
    p = list(Project.objects.values())
    return JsonResponse(p, safe=False)

def tasks(request, id):
    t = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html', {
        'task':t.title
    })
