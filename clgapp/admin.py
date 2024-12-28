from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import College, Department, Student

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'college')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department')


