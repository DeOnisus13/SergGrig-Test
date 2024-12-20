from django.contrib import admin

from workers.models import Group, Speciality, Worker


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "group", "payment", "speciality",)
