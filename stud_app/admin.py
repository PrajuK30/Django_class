from django.contrib import admin
from .models import *

# Register your models here.

# from .models import Course,Student,Grade,AllFieldType
from .models import AllFieldType,Student1,Course
# Register the models
# admin.site.register(Course)
# admin.site.register(Student)
# admin.site.register(Grade)
admin.site.register(AllFieldType)
#admin.site.register(Student1)
admin.site.register(Course)

@admin.register(Student1)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'date_of_birth')
    list_filter = ('age', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'age')
    
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name')
        }),
        ('Additional Info', {
            'fields': ('age', 'date_of_birth'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
    
    
    
    ## project##
    
    
    #admin.site.register(Project)
    #admin.site.register(TeamMember)
    #admin.site.register(ProjectTeam)
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
  
              list_display = ('name', 'description', 'get_team_members')
              search_fields = ('name', 'description')  


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # Displays team member details
    search_fields = ('first_name', 'last_name', 'email')  # Enables search by name or email


@admin.register(ProjectTeam)
class ProjectTeamAdmin(admin.ModelAdmin):
    list_display = ('project', 'member', 'role')  
    list_filter = ('role', 'project')  
    search_fields = ('project__name', 'member__first_name', 'member__last_name', 'role')  # Enables search by related project name, member name, or role

          
# admin.site.register(Project)
# admin.site.register(TeamMember)
# admin.site.register(ProjectTeam)
        
     
        
        
        
   

        
    
    
    
    
   












