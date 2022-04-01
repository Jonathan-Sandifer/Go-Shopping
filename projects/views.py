from django.contrib.auth.mixins import LoginRequiredMixin
from projects.models import Project
from tasks.models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect

# Create your views here.


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "projects/list.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "projects/detail.html"

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/create.html"
    fields = ["name", "description", "members"]

    def form_valid(self, form):
        project = form.save(commit=False)
        project.assignee = self.request.user
        form.save()
        return redirect("show_project", pk=project.id)
