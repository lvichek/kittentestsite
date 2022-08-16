from django.db import models

# Create your models here.

class task (models.Model):
    title = models.CharField('title', max_length = 50)
    taskname = models.TextField('todo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "a task"
        verbose_name_plural = "the tasks"    
   