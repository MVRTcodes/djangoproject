from django.http.response import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateTaskForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return render(request, 'about.html')

def projectsapi(request):
    p = list(Project.objects.values())
    return JsonResponse(p, safe=False)

def projects(request):
    p = Project.objects.all()
    t = Task.objects.all()
    return render(request, 'projects.html', {
        'projects': p,
        'tasks' : t
    })

def tasks(request, id):
    t = get_object_or_404(Task, id=id)
    return render(request, 'tasks.html', {
        'task':t.title
    })

def create_task(request):
    
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            Task.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    project=form.cleaned_data['project']
                )
            return redirect('/projects/')
    else:
        return render(request, 'create_task.html',{
            'form': CreateTaskForm
        })
        #return redirect('/projects')
