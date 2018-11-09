from django.contrib import admin

from . models import Course

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['course_name']
    ordering = ['course_name']
    list_display = [
        'course_name'
    ]

admin.site.register(Course,CourseAdmin)
