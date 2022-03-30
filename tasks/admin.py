from django.contrib import admin

# Register your models here.

from tasks.models import (
    Task,
)


class TaskAdmin(admin.ModelAdmin):
    pass


admin.site.register(Task, TaskAdmin)
