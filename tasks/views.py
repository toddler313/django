from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
# Create your views here.

# def index(request):
#     return HttpResponse("Welcome to Tasks!")

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # taskPriority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# tasks = ['Foo', 'Bar', 'Saar']
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks" : request.session["tasks"]
    })

def addTask(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():  # cleaned_data is only available if is_valid() is called and satisfied
            task = form.cleaned_data["task"]
            # priority = form.cleaned_data["taskPriority"]
            # tasks.append(task)
            request.session["tasks"] += [task]  # [task] is an array with one item "task"
            return HttpResponseRedirect(reverse("tasks:index"))
        else :
            return render(request, "tasks/addTask.html", {
                "form" : form
            })

    return render(request, 'tasks/addTask.html', {
        "form" : NewTaskForm()
    })