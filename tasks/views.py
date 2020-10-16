from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

tasks=[]

# Create your views here.
class NewTaskForm(forms.Form):
    task=forms.CharField(label="NewTask")

def task(request):
    return render(request, "task.html", {
        "task": tasks
    })

def add(request):
    if request.method=='POST':
        form=NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("task"))
        else:
            return render(request,"add.html",{'form':form})
    else:
        return render(request, "add.html", {
        "form": NewTaskForm()})
