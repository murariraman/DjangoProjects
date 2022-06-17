from django.contrib import admin
from Testapp.models import User

@admin.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display=['student_name', 'teacher_name', 'email', 'password']
# Register your models here.




