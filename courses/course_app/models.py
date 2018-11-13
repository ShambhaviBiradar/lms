from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)

    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Courses'
        verbose_name_plural = 'Courses'

class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    course = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="video_course",
        null=True,
        blank=True
    )

    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Videos'
        verbose_name_plural = 'Videos'

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()

    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'

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

    class Meta:
        verbose_name = 'Answers'
        verbose_name_plural = 'Answers'
