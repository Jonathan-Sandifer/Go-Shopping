from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from tasks.models import Task
from django.views.generic.list import ListView
# Create your views here.


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/create.html"
    fields = ["name", "start_date", "due_date", "project", "assignee"]

    def form_valid(self, form):
        task = form.save(commit=False)
        task.assignee = self.request.user
        task.save()
        return redirect("show_my_tasks")


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"

    def get_queryset(self):
        return Task.objects.filter(assignee=self.request.user)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    success_url = reverse_lazy("show_my_tasks")
