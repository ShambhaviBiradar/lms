''' course_app.admin.py '''

from django.contrib import admin

from . models import Course, Video

''' CourseAdmin '''
class CourseAdmin(admin.ModelAdmin):
    search_fields = ['course_name']
    ordering = ['course_name']
    list_display = [
        'course_name'
    ]

''' VideoAdmin '''
class VideoAdmin(admin.ModelAdmin):
    search_fields = ['video_name']
    ordering = ['video_name']
    list_display = [
        'video_id',
        'video_name',
        'created_at'
    ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
