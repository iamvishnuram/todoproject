from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from  django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from .models import Task
from .forms import TodoForm

class TaskListView(ListView):
    model = Task
    template_name = "index.html"
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model = Task
    template_name = "details.html"
    context_object_name = 'task'
    
class TaskUpdateView(UpdateView):
    model = Task
    template_name = "edit.html"
    context_object_name = 'task'
    fields = ('name', 'priority')

    def get_success_url(self):
        return reverse_lazy('details', kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy('home')



def index(request):
    details = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'index.html', {'task': details})


def delete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form':form, 'task':task} )
