from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)


    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)


class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=255)
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="video_course",
        null=True,
        blank=True
    )

    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer = models.TextField()
    question = models.ForeignKey(
        'Question',
        related_name='answer_question',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
