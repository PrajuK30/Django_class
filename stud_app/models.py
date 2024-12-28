from django.db import models

# Create your models here.

# Table for courses
# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=10, unique=True)
#     description = models.TextField(blank=True)
#     credits = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name


# # Table for students
# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=15, null=True, blank=True)
#     date_of_birth = models.DateField()
#     enrolled_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


# # Table for student grades (no ForeignKey)
# class Grade(models.Model):
#     student_name = models.CharField(max_length=100)
#     student_email = models.EmailField()
#     mobile_number = models.CharField(max_length=15,default="0000000000") 
#     course_name = models.CharField(max_length=100)
#     grade = models.CharField(max_length=2, choices=[
#         ('A', 'A'),
#         ('B', 'B'),
#         ('C', 'C'),
#         ('D', 'D'),
#         ('F', 'F'),
#     ])
   

#     def __str__(self):
#          return f"{self.student_name} - {self.course_name} - Grade: {self.grade}"
    
    
class AllFieldType(models.Model):
    char_field = models.CharField(max_length=100)
    text_field = models.TextField()
    integer_field = models.IntegerField()
    float_field = models.FloatField()
    date_field = models.DateField()
    boolean_field = models.BooleanField(default=False)
    email_field = models.EmailField()
    datetime_field = models.DateTimeField(auto_now_add=True)
    
class Student1(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField() #123
    date_of_birth = models.DateField()

    def __str__(self):
        return f"Student name - {self.first_name} {self.last_name}"
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student1, related_name='courses')
 
 
   
   
   

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_team_members(self):
        # Get all team members related to the project
        team_members = self.projectteam_set.all()  # Get all ProjectTeam objects related to this project
        return ", ".join([f"{team.member.first_name} {team.member.last_name}" for team in team_members])

    get_team_members.short_description = 'Team Members'


class TeamMember(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ProjectTeam(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_teams')
    member = models.ForeignKey(TeamMember, on_delete=models.CASCADE, related_name='team_projects')
    role = models.CharField(max_length=100, choices=[('Manager', 'Manager'), ('Developer', 'Developer'), ('Designer', 'Designer')])
    null=True,  # Allow null values
    blank=True

    def __str__(self):
        return f"{self.member} - {self.project} ({self.role})"
     